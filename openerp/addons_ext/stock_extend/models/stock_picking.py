# -*- coding: utf-8 -*-
'''
Created on 2016年4月25日

@author: cloudy
'''
from openerp import models,fields,api

class stock_picking(models.Model):
    _inherit = 'stock.picking'
    
    order_id = fields.Many2one('sale.order',string='sale order')
    purchase_id =fields.Many2one('purchase.order',string='purchase order')
    
    @api.model
    def create(self, vals):
        print vals
        origin = vals.get('origin',None)
        if origin:
            sale_obj = self.env['sale.order'].search([('name','=',origin)])
            if sale_obj:
                vals['order_id'] = sale_obj.id
            purchase_obj = self.env['purchase.order'].search([('name','=',origin)])
            if purchase_obj:
                vals['purchase_id'] = purchase_obj.id
        return super(stock_picking,self).create(vals)