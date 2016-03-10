# -*- coding: utf-8 -*-
'''
Created on 2016年2月23日

@author: cloudy
'''
from openerp import fields,models,api

class stock_picking(models.Model):
    _inherit = 'stock.picking'
    
    sale_id = fields.Many2one('sale.order',string="Sale Order")
    purchase_id = fields.Many2one('purchase.order',string="Purchase Order")
    
    _defaults = {
        'move_type':'one',
    }


    
    