# -*- coding: utf-8 -*-
'''
Created on 2016年3月26日

@author: cloudy
'''
from openerp import models,fields


class purchase_order(models.Model):
    _inherit = 'purchase.order'
    
    _defaults ={
        'picking_type_id':1,
    }