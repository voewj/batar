# -*- coding: utf-8 -*-
'''
Created on 2016年4月19日

@author: cloudy
'''
from openerp import models,fields,api,_
from openerp.exceptions import UserError
    
class product_discount(models.Model):
    _name ='product.discount'
    Applied_On = [('3_global', 'global'),
                  ('2_product_category', 'product category'), 
                  ('1_product', 'product'), 
                  ('0_product_variant', 'product variant')]
    applied_on = fields.Selection(Applied_On,string='applied on')
    name = fields.Char(string='name')
    partner_id = fields.Many2one('res.partner',string='customer')
    categ_id = fields.Many2one('product.category',string='product category')
    product_tmpl_id = fields.Many2one('product.template',string='product template',ondelete='cascade')
    product_id = fields.Many2one('product.product',string='product')
    date_start = fields.Date(string='start date')
    date_end = fields.Date(string='end date')
    min_quantity = fields.Float(string='min quantity',default=1.0)
    item_fee = fields.Float(related='product_id.item_fee', string='item fee discount')
    weight_fee =fields.Float(related='product_id.weight_fee', string='weight fee discount')
    item_fee_discount = fields.Float(string='item fee discount')
    weight_fee_discount =fields.Float(string='weight fee discount')
    item_fee_discount_percent = fields.Integer(string='item fee discount percent')
    weight_fee_discount_percent =fields.Integer(string='weight fee discount percent')
    active = fields.Boolean(string='active')
    
    @api.onchange('item_fee_discount','weight_fee_discount')
    def change_discount(self):
        '''工费变化'''
        
    @api.model
    def create(self, vals):
        print vals
        name =  _('all products')
        
        categ_id = vals.get('categ_id',None)
        if categ_id:
            name = self.env['product.category'].search([('id','=',categ_id)]).name
        product_tmpl_id = vals.get('product_tmpl_id',None)
        if product_tmpl_id:
            name = self.env['product.template'].search([('id','=',product_tmpl_id)]).name
        product_id = vals.get('product_id',None)
        if product_id:
            name = self.env['product.product'].search([('id','=',product_id)]).name
       
        
        vals['active'] = True
        vals['name'] =  name 
        print vals
        return super(product_discount,self).create( vals)
    
    
    
    