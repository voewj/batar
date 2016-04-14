# -*- coding: utf-8 -*-
'''
Created on 2016年3月28日

@author: cloudy
'''
from openerp import models,fields


class stock_warehouse(models.Model):
    _inherit = 'stock.warehouse'
    
    is_quality = fields.Boolean(string='is quality stock warehouse')
    is_return = fields.Boolean(string="is return warehouse")
    _defaults = {
        'is_quality':False,
    }