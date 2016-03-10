# -*- coding: utf-8 -*-
'''
Created on 2016年3月8日

@author: cloudy
'''
from openerp import models,fields,_

class product_recycling_fee(models.Model):
    _name = 'product.recycling.fee'
    
    name = fields.Char(string='recycling name',default=_('price difference'))
    product_id = fields.Many2one('product.template',string='products',domain=[('type','=','recycling')])
    price_unit = fields.Float(string='price unit')
