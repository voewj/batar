# -*- coding: utf-8 -*-
'''
Created on 2016年3月18日

@author: cloudy
'''
from openerp import models,fields,api

class product_attribute(models.Model):
    _inherit = 'product.attribute'
    
    code = fields.Char(string='product attribute code')
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'code must be unique!'),
       
    ]
    @api.multi
    def write(self, vals):
        code = vals.get('code','')
        if code:
            code = code.strip()
            vals['code'] = code.upper()
        return super(product_attribute,self).write(vals)
    @api.model
    def create(self, vals):
        code = vals.get('code','')
        code = code.strip()
        vals['code'] = code.upper()
        return super(product_attribute,self).create(vals)
    