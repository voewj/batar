# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api
# import openerp.addons.decimal_precision as dp

class product_template(models.Model):
    _inherit = "product.template"
    
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string='weight fee')
    ponderable = fields.Boolean(string='ponderable')
    
    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    

        