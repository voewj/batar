# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api
# import openerp.addons.decimal_precision as dp

class product_template(models.Model):
    _inherit = "product.template"
    
    standard_weight = fields.Float(string="Standard Weight")
    item_fee = fields.Float(string="Item Fee")
    ponderable = fields.Boolean(string='ponderable')

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
