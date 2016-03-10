# -*- coding: utf-8 -*-
'''
Created on 2016年2月27日

@author: cloudy
'''

from openerp import fields,models,api

class customer_discount_product(models.Model):
    _name = "customer.discount.product"
    
    partner_id = fields.Many2one('res.partner',String="Res Partner",search="[('supplier','=',True)]")
    customer_code = fields.Char(related='partner_id.customer_code',string="Customer Code")
    product_id = fields.Many2one('product.product',string="Products")
    default_code = fields.Char(related='product_id.default_code',string="Default Code")
#     standrad_weight = fields.Float(related='product_id.standrad_weight',string="Standard Weight")
#     base_weight_fee = fields.Float(related='product_id.base_weight_fee',string="Base Weight Fee")
#     additional_fee = fields.Float(related='product_id.additional_fee',string="Additional Fee")
#     item_fee = fields.Float(related='product_id.item_fee',string="Item Fee")
#     discount = fields.Float(related='product_id.discount',string="Discount")
    discount_weight_fee = fields.Float(string="Discount Weight Fee")
    discount_weight_fee_enable = fields.Boolean(string="Discount Weight Fee Enable")
    discount_item_fee = fields.Float(string="Discount Item")
    discount_item_fee_enable = fields.Boolean(string="Discount Item Enable")
    discount_item_percent = fields.Float(string="Discount Item Percent")
    discount_item_percent_enable = fields.Boolean(string="Discount Item Percent")
    _defaults = {
        'discount_weight_fee_enable':True,
        'discount_item_fee_enable':False,
        'discount_item_percent_enable':False,
    }
    