# -*- coding: utf-8 -*-
'''
Created on 2016年5月2日

@author: cloudy
'''
from openerp import models,fields,api,_


class delivery_bill(models.Model):
    _name = 'delivery.bill'
   
    
    
    _STATE = [
        ('draft','draft'),
        ('error','error'),
        ('confirm','confirm')
    ]
    name = fields.Char(string='delivery bill name')
    charge_man = fields.Many2one('res.users',string='ERP chage man')
    purchase_number = fields.Char(string='purchase order')
    purchase_id = fields.Many2one('purchase.order',string='purchase order')
    partner_id = fields.Many2one(related='purchase_id.partner_id',store=True,string='partner')
    partner_person = fields.Char(string='supplier charge man')
    partner_mobile = fields.Char(string='supplier charge man mobile')
    delivery_method = fields.Char(string='delivery method')
    delivery_man = fields.Char(string='delivery charge man')
    delivery_mobile = fields.Char(string='delivery charge man mobile')
    state = fields.Selection(_STATE,string='state',default='draft')
    line_id = fields.One2many('delivery.bill.line','delivery_id',string='delivery bill line')
    picking_id = fields.Many2one('stock.picking',string='stock picking')
    location_src_id = fields.Many2one('stock.location',string='source location')
    location_dest_id = fields.Many2one('stock.location',string='dest location')
    
    
class delivery_bill_line(models.Model):
    _name = 'delivery.bill.line'
    delivery_id = fields.Many2one('delivery.bill',string='delivery bill')
    partner_id = fields.Many2one(related='delivery_id.partner_id',string='partner')
    name = fields.Char(string='delivery bill line')
    pkg_number = fields.Char(string='package number')
    product_id = fields.Many2one('product.product',string='product')
    product_qty = fields.Float(string='product quantity')
    supplier_code = fields.Char(string='supplier code')
    default_code = fields.Char(string='default code')
    net_weight = fields.Float(string='net weight')
    gross_weight = fields.Float(string='gross weight')
    note = fields.Text(string='note')
    
    
    