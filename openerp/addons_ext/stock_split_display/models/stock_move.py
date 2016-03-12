# -*- coding: utf-8 -*-
'''
Created on 2016年3月11日
des:库存分仓显示
@author: cloudy
'''
from openerp import models,fields

class stock_move_detail(models.TransientModel):
    _name = 'stock.move.detail'
    
    product_id = fields.Many2one('product.product',string='products')
    default_code = fields.Char(related='product_id.default_code',sting='default code')
    attribute_value_ids = fields.Many2many(related='product_id.attribute_value_ids',string='product attributes')
    lst_price = fields.Float(related='product_id.lst_price',string='lst price')
    hand_qty = fields.Float(compute='_compute_hand_qty',string='hand qty')
    lock_qty = fields.Float(compute='_compute_lock_qty',string='locked qty')
    hand_weight = fields.Float(compute='_compute_hand_weight',string='hand weight')
    lock_weight = fields.Float(compute='_compute_locked_weight',string='locked weight')
    warehouse_id = fields.Many2one('stock.warehouse')
    