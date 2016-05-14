# -*- coding: utf-8 -*-
'''
Created on 2016年3月18日

@author: cloudy
'''
from openerp import models,fields,api
from openerp.exceptions import UserError
from openerp.tools.common_ext import GetNextSequence
import re

class product_attribute(models.Model):
    _inherit = 'product.attribute'
    code = fields.Char(string='product attribute code')
   
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'code must be unique!'), 
    ]
    @api.multi
    def write(self, vals):
        code = vals.get('code','')
        if code:
            vals['code']= code.strip()
        return super(product_attribute,self).write(vals)
    @api.model
    def create(self, vals):
        code = vals.get('code','')
        attributeObj  = self.env['product.attribute'].search([],limit=1,order='id desc')
        sequence = 1
        if attributeObj:
            sequence = GetNextSequence(sequence)
        vals['sequence'] = sequence
        if code:
            vals['code'] = code.strip()
        return super(product_attribute,self).create(vals)

class product_attribute_value(models.Model):
    _inherit = 'product.attribute.value'
    _order = 'id desc'

    name = fields.Char(translate=False)

    @api.multi
    def write(self, vals):
        if self.attribute_id.code =='weight':
            name = vals.get('name','')
            m = re.match(r"(^[0-9]\d*\.\d|\d+)",name)
            if not m:
                raise UserError(_('The value of the weight attribute can only be: 10 or 10g')) 
            vals['name']= '%sg' % m.group(1)
        return super(product_attribute_value,self).write(vals)
    
    @api.model
    def create(self, vals):
        attribute_id = vals.get('attribute_id',None)
        if attribute_id:
            attributeValueObj = self.env['product.attribute.value'].search([('attribute_id','=',attribute_id)],limit=1)
            sequence = 1
            if attributeValueObj:
                sequence = GetNextSequence(sequence)
            vals['sequence'] = sequence
       
        attr_obj = self.env['product.attribute'].search([('id','=',attribute_id)])
        if attr_obj.code == 'weight':
            name = vals.get('name','')
            m = re.match(r"(^[0-9]\d*\.\d|\d+)",name)
            if not m:
                raise UserError(_('The value of the weight attribute can only be: 10 or 10g')) 
            vals['name']= '%sg' % m.group(1)
        return super(product_attribute_value,self).create(vals)
