# -*- coding: utf-8 -*-
'''
Created on 2016年4月25日

@author: cloudy
'''
from openerp import models,fields,api

class stock_pack_operation(models.Model):
    _inherit = 'stock.pack.operation'
    
    real_time_price_unit = fields.Float(string='real time price unit')
    standrad_weight = fields.Float(related='product_id.standard_weight',string="Standard Weight")
    all_weights = fields.Float(string='all line weight')
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string="weight fee")
    additional_fee = fields.Float(string='additional fee')
    
#     @api.v8
#     @api.onchange('product_id')
#     def product_id_change(self):
#         ''''''
#         if self.product_id:
#             pass
            
