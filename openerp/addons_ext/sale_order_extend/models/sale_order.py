# -*- coding: utf-8 -*-
'''
Created on 2016年2月24日

@author: cloudy
'''

from openerp import fields,models

class sale_order_line(models.Model):
    _inherit = "sale.order.line"
              
    second_product_uom = fields.Many2one('product.uom',string='Second Product Uom')
    second_product_uom_qty = fields.Float(string='Second Product Uom Weight')
#     sale_man_id = fields.Many2one('res.users',string='Sale man who create order line for customer')
