# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models

class prdouct_product(models.Model):
    _inherit = "product.product"
    

    standard_weight = fields.Float(related='product_tmpl_id.standard_weight',store=True,string="Standard Weight")
    item_fee = fields.Float(related='product_tmpl_id.item_fee',store=True,string="Item Fee")
    ponderable = fields.Boolean(related='product_tmpl_id.ponderable',store=True,string='ponderable')

    _defaults = {
        'type': "product",
        'ponderable':True,
    }