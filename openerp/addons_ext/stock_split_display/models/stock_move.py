# -*- coding: utf-8 -*-
'''
Created on 2016年3月11日
des:库存分仓显示
@author: cloudy
'''
from openerp import models,fields,api

class stock_warehouse(models.Model):
    _inherit = 'stock.warehouse'
    en_code = fields.Char(string='stock warehouse english code')
 
    
class stock_move_detail(models.TransientModel):
    _name = 'stock.move.detail'
    
    @api.multi
    @api.depends('warehouse_id')
    def name_get(self):
        result = []
        for line in self:
            name = "%s" % (line.warehouse_id.name)
            result.append((line.id,name))
        return result
    product_id = fields.Many2one('product.product',string='products')
    default_code = fields.Char(related='product_id.default_code',sting='default code')
    attribute_value_ids = fields.Many2many(related='product_id.attribute_value_ids',string='product attributes')
    lst_price = fields.Float(related='product_id.lst_price',string='lst price')
    hand_qty = fields.Float(compute='_compute_qty_and_weight',string='hand qty')
    lock_qty = fields.Float(compute='_compute_qty_and_weight',string='locked qty')
    hand_weight = fields.Float(compute='_compute_qty_and_weight',string='hand weight')
    lock_weight = fields.Float(compute='_compute_qty_and_weight',string='locked weight')
    warehouse_id = fields.Many2one('stock.warehouse')
    en_code = fields.Char(related='warehouse_id.en_code',string='stock warehouse english code')
    
    
    def _compute_qty_and_weight(self):
        ''''''
        pass
    