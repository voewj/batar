# -*- coding: utf-8 -*-
'''
Created on 2016年3月18日

@author: cloudy
'''
from openerp import models,fields,api
from openerp.exceptions import UserError, ValidationError
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
        sequence_list  = self.env['product.attribute'].search([])
        sequence = 1
        sequence_list = [line.sequence for line in sequence_list]
        if sequence_list:
           
            sequence = max(sequence_list) + 1
        
        vals['sequence'] = sequence
        if code:
            vals['code'] = code.strip()
        return super(product_attribute,self).create(vals)

class product_attribute_value(models.Model):
    _inherit = 'product.attribute.value'
    _order = 'id desc'

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
        if attribute_id == self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_material')[1]:
            material_list = self.env['product.attribute.value'].search([('attribute_id','=',attribute_id)])
            sequence_list = [line.sequence for line in material_list]
            if sequence_list:
                sequence = max(sequence_list) +1
            else:
                sequence = 10
            vals['sequence'] = sequence
        elif attribute_id == self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_style')[1]:
            material_list = self.env['product.attribute.value'].search([('attribute_id','=',attribute_id)])
            sequence_list = [line.sequence for line in material_list]
            if sequence_list:
                sequence = max(sequence_list) +1
            else:
                sequence = 1
            vals['sequence'] = sequence
        elif attribute_id == self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_model')[1]:
            material_list = self.env['product.attribute.value'].search([('attribute_id','=',attribute_id)])
            sequence_list = [line.sequence for line in material_list]
            if sequence_list:
                sequence = max(sequence_list) +1
            else:
                sequence = 1
            vals['sequence'] = sequence
        else:
            material_list = self.env['product.attribute.value'].search([('attribute_id.code','not in',('material','style','model'))],limit=1)
            sequence_list = [line.sequence for line in material_list]
            if sequence_list:
                sequence = max(sequence_list) +1
            else:
                sequence = 1
            vals['sequence'] = sequence
        attr_obj = self.env['product.attribute'].search([('id','=',attribute_id)])
        if attr_obj.code == 'weight':
            name = vals.get('name','')
            m = re.match(r"(^[0-9]\d*\.\d|\d+)",name)
            if not m:
                raise UserError(_('The value of the weight attribute can only be: 10 or 10g')) 
            vals['name']= '%sg' % m.group(1)
        return super(product_attribute_value,self).create(vals)
