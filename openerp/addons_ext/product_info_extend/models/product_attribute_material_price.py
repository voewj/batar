# -*- coding: utf-8 -*-
'''
Created on 2016年3月18日

@author: cloudy
'''
from openerp import models,fields,api,_
from openerp.exceptions import UserError


class product_attribute_material_price(models.Model):
    _name = 'product.attribute.material.price'
    
    attribute_id = fields.Many2one('product.attribute')
    attribute_value_id = fields.Many2one('product.attribute.value',string='product attribute value')
    active = fields.Boolean(string='active')
    price_unit = fields.Float(string='price unit')
    ornament_price = fields.Float(string="ornament price")
    
    _sql_constraints = [
        ('price_unit', 'CHECK(price_unit > 0.0)','price_unit must be greater than 0.0!'),
        ('ornament_price', 'CHECK(ornament_price > 0.0)','ornament_price must be greater than 0.0!'),
    ]

    _defaults = {
        'active':False,
    }
    
    @api.multi
    @api.depends('attribute_id','attribute_value_id')
    def name_get(self):
        result = []
        for line in self:
            name = "%s:%s" % (line.attribute_id.name,line.attribute_value_id.name)
            result.append((line.id,name))
        return result
    
    @api.model
    def create(self, vals):
        '''保存前使之前的价格无效'''
        
        vals['active'] = True
        attribute_id = vals.get('attribute_id',None)
        attribute_value_id = vals.get('attribute_value_id',None)  
         
        if not( attribute_id and attribute_value_id):
            raise UserError(_('attribute or attribute value invalid'))
        records = self.env['product.attribute.material.price'].search([('attribute_id','=',attribute_id),('attribute_value_id','=',attribute_value_id)])
        records.write({'active':False})
        return super(product_attribute_material_price,self).create( vals)