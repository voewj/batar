# -*- coding: utf-8 -*-
'''
Created on 2016年2月24日

@author: cloudy
'''

from openerp import fields,models,api

class sale_order_line(models.Model):
    _inherit = "sale.order.line"
            
    real_time_price_unit = fields.Float(compute="_real_time_price_unit",string='real time price unit')
    standrad_weight = fields.Float(related='product_id.standard_weight',store=True,string="Standard Weight")
    all_weights = fields.Float(string='all line weight')
    item_fee = fields.Float(related='product_id.item_fee',store=True,string="Item Fee")
    weight_fee = fields.Float(related='product_id.weight_fee',store=True,string="weight fee")
    ponderable = fields.Boolean(related='product_id.ponderable',string="ponderable")
    sale_price = fields.Char(related='product_id.sale_price',string='display sale price')
    
    defaults = {
        'picking_policy':'one',
        'all_weights':0,
    }
    @api.one
    def _real_time_price_unit(self):
        ''''''
        self.ensure_one()
        if self.product_id:
            #订单完成价格不变
            if self.state !='done':
                self.real_time_price_unit = self.product_id.real_time_price_unit
                self._compute_amount()
       
    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id','all_weights')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)  
            
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,\
                                             product=line.product_id, partner=line.order_id.partner_id,ponderable=line.ponderable,
                                             real_time_price_unit=line.real_time_price_unit,item_fee=line.item_fee,\
                                             weight_fee=line.weight_fee, standrad_weight=line.standrad_weight,all_weights=line.all_weights)
            
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            