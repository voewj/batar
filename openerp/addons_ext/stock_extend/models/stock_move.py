# -*- coding: utf-8 -*-
'''
Created on 2016年2月29日

@author: cloudy
'''
from openerp import models,fields,api


class stock_move(models.Model):
    _inherit = 'stock.move'

    order_line_id = fields.Many2one(related='procurement_id.order_line_id',string='sale order line')
    real_time_price_unit = fields.Float(related='order_line_id.real_time_price_unit',string='real time price unit')
    standrad_weight = fields.Float(related='product_id.standard_weight',string="Standard Weight")
    all_weights = fields.Float(string='all line weight')
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string="weight fee")
    ponderable = fields.Boolean(related='product_id.ponderable',string="ponderable")
    price_subtotal = fields.Float(realted='order_line_id.price_subtotal',string='sub total')
    
    
    @api.onchange('all_weights')
    def sale_change(self):
        ''''''
        for line in self:
            if self.order_line_id:
                self.order_line_id.all_weights = line.all_weights
                
    @api.model
    def create(self, vals):
        order_line_id = vals.get('order_line_id','')
        if order_line_id:
            vals['item_fee'] = order_line_id.item_fee
            vals['weight_fee'] = order_line_id.weight_fee
        return super(stock_move,self).create(vals)
    
    
    @api.multi
    def write(self, vals):
        product_uom_qty = vals.get('product_uom_qty',0)
        if product_uom_qty:
            self.procurement_id.write({'product_qty':product_uom_qty})
            self.order_line_id.write({'product_uom_qty':product_uom_qty})
        return super(stock_move,self).write( vals)

