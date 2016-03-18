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
    
    defaults = {
        #'real_time_price_unit':lambda self:self.product_id.real_time_price_unit,
        'picking_policy':'one',
        'all_weights':0,
    }
    @api.one
    @api.depends('product_id')
    def _real_time_price_unit(self):
        ''''''
        self.ensure_one()
        if self.product_id:
            print self.product_id
            self.real_time_price_unit = self.product_id.real_time_price_unit
       
   
    @api.one
    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id','item_fee','weight_fee','real_time_price_unit','standrad_weight','all_weights')
    def _compute_amount(self):
        
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            print line.ponderable,line.real_time_price_unit,line.item_fee,line.weight_fee,line.standrad_weight,line.all_weights
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id,ponderable=line.ponderable,real_time_price_unit=line.real_time_price_unit,item_fee=line.item_fee,weight_fee=line.weight_fee, standrad_weight=line.standrad_weight,all_weights=line.all_weights)
            print taxes
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
