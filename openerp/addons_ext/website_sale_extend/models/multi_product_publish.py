# -*- coding: utf-8 -*-
'''
Created on 2016年2月29日

@author: cloudy
'''

from openerp import models


class product_product(models.Model):
    _inherit = 'product.product'
    
    def multi_product_publish_button(self):
        pass