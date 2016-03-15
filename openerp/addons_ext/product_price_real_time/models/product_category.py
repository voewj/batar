# -*- coding: utf-8 -*-
'''
Created on 2016年3月15日

@author: cloudy
'''
from openerp import models,fields

class product_category(models.Model):
    _inherit = 'product.category'
    
    sub_top = fields.Boolean(string='product category sub top',help="Basic unit price (g) for the classification of the unit price")
    _defaults ={
        'sub_top':False,
    }