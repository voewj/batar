# -*- coding: utf-8 -*-
'''
Created on 2016年3月15日

@author: cloudy
'''

from openerp import fields,models,api


class product_price_real_time(models.Model):
    _name = 'product.price.real.time'
    _order = 'id desc,category_id'
    
    user_id = fields.Many2one('res.users',string='record input user',default=lambda self: self.env.user)
    start_time = fields.Datetime(string='start time')
    end_time = fields.Datetime(string='end time')
    active = fields.Boolean(string='active')
    real_time_price_unit = fields.Float(string='real time price unit')
    category_id = fields.Many2one('product.category',string='product category')
    
    _defaults = {
        'active':True,
    }
    
    
