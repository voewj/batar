# -*- coding: utf-8 -*-
'''
Created on 2016年2月27日

@author: cloudy
'''
from openerp import fields,models,api

class res_partner(models.Model):
    _inherit = 'res.partner'
    
    @api.depends('discount_product_line')
    def _get_discount_product_count(self):
        '''Get Discount Product Count'''
        for line in self:
            
            line.update({
                'discount_product_count':len(line.discount_product_line) or 0
            })
        
    discount_product_line = fields.One2many('customer.discount.product', 'partner_id',string="Customer Discount Product")  
    discount_product_count = fields.Integer(string="Discount Product Count",compute='_get_discount_product_count',readonly=True)