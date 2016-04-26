# -*- coding: utf-8 -*-
'''
Created on 2016年4月25日

@author: cloudy
'''
from openerp import models,fields,api

class stock_pack_operation(models.Model):
    _inherit = 'stock.pack.operation'
    
    real_time_price_unit = fields.Float(string='real time price unit')
    standrad_weight = fields.Float(related='product_id.standard_weight',string="Standard Weight")
    all_weights = fields.Float(string='all line weight')
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string="weight fee")
    additional_fee = fields.Float(string='additional fee')
    
#     @api.v8
#     @api.onchange('product_id')
#     def product_id_change(self):
#         ''''''
#         if self.product_id:
#             pass

    
    @api.onchange('all_weights') 
    def onchange_all_weights(self):
        ''''''
        
    @api.model
    def create(self, vals):
        '''
        dict: {'pack_lot_ids': [], 'fresh_record': False, 'package_id': False, 'location_dest_id': 9, 'product_id': 9, 'product_qty': 1000.0, 'product_uom_id': 1, 'location_id': 12, 'picking_id': 9, 'owner_id': False}'''
        picking_id = vals.get('picking_id',None)
        stock_picking_obj  =self.env['stock.picking'].search([('id','=',picking_id)])
        partner_id = stock_picking_obj.partner_id
        if partner_id:
            vals['owner_id'] = partner_id.id
        product_id = vals.get('product_id',None)
        move_lines = stock_picking_obj.move_lines_related
        for line in move_lines:
            if line.product_id.id == product_id:
                vals['real_time_price_unit'] = line.real_time_price_unit
                vals['standrad_weight'] = line.standrad_weight
                vals['item_fee'] = line.item_fee
                vals['weight_fee'] = line.weight_fee
                vals['additional_fee'] = line.additional_fee
                
                
        return super(stock_pack_operation,self).create( vals)