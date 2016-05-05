# -*- coding: utf-8 -*-
'''
Created on 2016年4月16日

@author: cloudy
'''
from openerp import models,fields,api,_
from openerp.exceptions import UserError



class customer_ornament_price(models.Model):
    '''设置客户的饰品价格'''
    _name ='customer.ornament.price'
    

       
    @api.one
    @api.depends('material_price','ornament_price')
    def _get_price_uint(self):
        ''''''
        self.price_unit = self.material_price+self.ornament_price
        
        
    partner_id = fields.Many2one('res.partner',string='customer')
    active = fields.Boolean(string='active')
    attribute_value_id = fields.Many2one('product.attribute.value',string='product attribute value')
    attribute_id = fields.Many2one('product.attribute',\
                                   default= lambda self:self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_material')[1],string='product attribute')
    material_price = fields.Float(string='material price')
    sys_ornament_price = fields.Float(string='system ornament price')
    ornament_price = fields.Float(string='ornament price')
    price_unit = fields.Float(compute='_get_price_uint',string='price unit')
    
    
    @api.onchange('attribute_value_id')
    def change_attribute_value(self):
        '''属性更改'''
        if self.attribute_value_id:
            obj = self.env['product.attribute.material.price'].search([('active','=',True),('attribute_value_id','=',self.attribute_value_id.id)])
            if obj:
                self.material_price = obj.material_price
                self.sys_ornament_price = obj.ornament_price
                self.ornament_price = obj.ornament_price
            else:
                raise UserError(_('You must set material price before'))
        
                
    @api.model
    def create(self, vals):
        vals['active'] = True
        partner_id = vals.get('partner_id',None)
        attribute_value_id = vals.get('attribute_value_id',None)  
        if not attribute_value_id:
            raise UserError(_('attribute value invalid'))
        records = self.env['customer.ornament.price'].search([('partner_id','=',partner_id),('active','=',True),('attribute_value_id','=',attribute_value_id)])
        obj = self.env['product.attribute.material.price'].search([('active','=',True),('attribute_value_id','=',attribute_value_id)])
        if obj:
            vals['material_price'] = obj.material_price
            vals['sys_ornament_price'] = obj.ornament_price
        if records:
            records.write({'active':False})
        #设置默认的饰品价，
        attribute_value_id = vals.get('attribute_value_id',None)
        return super(customer_ornament_price,self).create(vals)

    