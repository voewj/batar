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
    item_fee = fields.Float(related='product_id.item_fee', string='item fee')
    weight_fee =fields.Float(related='product_id.weight_fee', string='weight fee')
    item_fee_discount = fields.Float(string='item fee discount')
    weight_fee_discount =fields.Float(string='weight fee discount')
    item_fee_discount_percent = fields.Float(string='item fee discount percent')
    weight_fee_discount_percent =fields.Float(string='weight fee discount percent')
    is_percent = fields.Boolean(string='discount depend on percent')
    active = fields.Boolean(string='active')
    
    _sql_constraints = [
        ('uniq', 'unique(partner_id,categ_id,product_tmpl_id,product_id,active)', 'code must be unique!'), 
    ]
    
    @api.onchange('product_id','item_fee_discount_percent','weight_fee_discount_percent')
    def product_id_change(self):
        ''''''
        if self.product_id:
            self.item_fee = self.product_id.item_fee
            self.weight_fee = self.product_id.weight_fee
        if self.weight_fee_discount_percent:
            if int(self.weight_fee_discount_percent*100) >=100 or  int(self.weight_fee_discount_percent*100) <1:
                raise  UserError(_('weight fee discount percent range is [0,1]'))
        if self.item_fee_discount_percent:
            if int(self.item_fee_discount_percent*100) >=100 or  int(self.item_fee_discount_percent*100) <1:
                raise  UserError(_('item fee discount percent range is [0,1]'))

    
    @api.model
    def create(self, vals):
        name =  _('no select')
        partner_id = vals.get('partner_id',None)
        
        applied_on = vals.get('applied_on','')
        if '3_global' == applied_on:
            name =  _('all products')
            obj = self.search([('partner_id','=',partner_id),('applied_on','=','3_global')])
            if obj:
                obj.write({'active':False})
        elif '2_product_category' == applied_on:
            categ_id = vals.get('categ_id',None)
            if categ_id:
                name  = self.env['product.category'].search([('id','=',categ_id)]).name
                obj = self.search([('partner_id','=',partner_id),('categ_id','=',categ_id)])
                if obj:
                    obj.write({'active':False})
        elif '1_product' == applied_on:
            product_tmpl_id = vals.get('product_tmpl_id',None)
            if product_tmpl_id:
                name = self.env['product.template'].search([('id','=',product_tmpl_id)]).name
                obj = self.search([('partner_id','=',partner_id),('product_tmpl_id','=',product_tmpl_id)])
                if obj:
                    obj.write({'active':False})
        elif '0_product_variant' == applied_on:
            product_id = vals.get('product_id',None)
            if product_id:
                name = self.env['product.product'].search([('id','=',product_id)]).name
                obj = self.search([('partner_id','=',partner_id),('product_id','=',product_id)])
                if obj:
                    obj.write({'active':False})
                   
        vals['active'] = True
        vals['name'] =  name 
        return super(product_discount,self).create(vals)
    
    
    
    