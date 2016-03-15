# -*- coding: utf-8 -*-
'''
Created on 2016年2月24日

@author: cloudy
'''

from openerp import fields,models

class sale_order_line(models.Model):
    _inherit = "sale.order.line"
            
    real_time_price_unit = fields.Float(string='real time price unit')
    
    defaults = {
        'real_time_price_unit':lambda self:self.product_id.real_time_price_unit,
    }

