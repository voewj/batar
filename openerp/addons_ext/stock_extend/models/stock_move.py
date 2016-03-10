# -*- coding: utf-8 -*-
'''
Created on 2016年2月29日

@author: cloudy
'''
from openerp import models,fields


class stock_move(models.Model):
    _inherit = 'stock.move'

    standrad_weight = fields.Float(related='product_id.standard_weight',store=True,string="Standard Weight")
    item_fee = fields.Float(related='product_id.item_fee',store=True,string="Item Fee")

    
