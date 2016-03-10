# -*- coding: utf-8 -*-
'''
Created on 2016年3月1日

@author: cloudy
'''

from openerp import models,fields

class stock_location_detail(models.Model):
    _name = 'stock.location.detail'
    
    location_id = fields.Many2one('stock.location',string="stock location")
    name = fields.Char(string="Location Detail Name")
    code = fields.Char(string="Location Code")
    position_x = fields.Integer(string="Position X")
    position_y = fields.Integer(string="Position Y")
    position_z = fields.Integer(string="Position z")
    position_str_x = fields.Char(string="Position String X")
    position_str_y = fields.Char(string="Position String Y")
    position_str_z = fields.Char(string="Position String Z")
    parent_id = fields.Many2one('stock.location.detail',string="Parent Position")
    product_id = fields.Many2one('product.product',string="product")

