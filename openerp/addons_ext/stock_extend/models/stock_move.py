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
    all_weights = fields.Float(related='order_line_id.all_weights',string='all line weight')
    item_fee = fields.Float(related='order_line_id.item_fee',string="Item Fee")
    weight_fee = fields.Float(related='order_line_id.weight_fee',string="weight fee")
    ponderable = fields.Boolean(related='product_id.ponderable',string="ponderable")
    price_subtotal = fields.Float(realted='order_line_id.price_subtotal',string='sub total')
    

    @api.multi
    def write(self, vals):
        product_uom_qty = vals.get('product_uom_qty',0)
        if product_uom_qty:
            self.procurement_id.write({'product_qty':product_uom_qty})
            self.order_line_id.write({'product_uom_qty':product_uom_qty})
        return super(stock_move,self).write( vals)

