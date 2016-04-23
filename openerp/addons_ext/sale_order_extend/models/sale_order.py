# -*- coding: utf-8 -*-
'''
Created on 2016年2月24日

@author: cloudy
'''

from openerp import fields,models,api,_
from openerp.exceptions import UserError


 
class sale_order(models.Model):
    _inherit = 'sale.order'
      
    material_price_line = fields.One2many('sale.order.material.price','order_id',string='sale order material price')
    
    @api.onchange('partner_id')
    def partner_change(self):
        '''根据客户获得客户的基础价格信息'''
        
        material_price_line = []
        if self.partner_id:
           
            attribute_id = self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_material')[1]
            attribute_values = self.env['product.attribute.value'].search([('attribute_id','=',attribute_id)])
            for attribute_value in attribute_values:
                customer_ornament_price_obj=self.env['customer.ornament.price'].search([('partner_id','=',self.partner_id.id),('attribute_value_id','=',attribute_value.id),('active','=',True)])
                price_unit = 0
                if customer_ornament_price_obj:
                    price_unit = customer_ornament_price_obj.price_unit
                else:
                    price_unit = self.env['product.attribute.material.price'].search([('active','=',True),('attribute_value_id','=',attribute_value.id)]).price_unit
                values = {
                   
                    'attribute_value_id':attribute_value.id,
                    'price_unit':price_unit
                }
                material_price_line.append((0,0,values))
            self.material_price_line = material_price_line
            
            
                
                
            
            
class sale_order_material_price(models.Model):
    _name ='sale.order.material.price'

    order_id = fields.Many2one('sale.order',ondelete='cascade',string='sale order')
    attribute_value_id = fields.Many2one('product.attribute.value',string='product attribute value')
    attribute_id = fields.Many2one('product.attribute',\
                                   default= lambda self:self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_material')[1],string='product attribute')
    price_unit = fields.Float(string='real time material price')
    _sql_constraints = [
        ('unique', '(order_id, attribute_value_id)','one order attribute value must unique!'),
    ]

