# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api
import re
import datetime
code_format = "%Y%m%d%H%M%S"


class prdouct_product(models.Model):
    _inherit = "product.product"
    

    standard_weight = fields.Float(compute='_compute_attribute',string="Standard Weight")
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string="weight fee")
    ponderable = fields.Boolean(related='product_tmpl_id.ponderable',store=True,string='ponderable')
    real_time_price_unit = fields.Float(compute='_compute_attribute',string='real time price unit')
    shang_code = fields.Char(string='show king code')
    sale_price = fields.Char(compute='_compute_sale_price',string='display sale price')
    

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    
    @api.multi
    def _compute_sale_price(self):
        '''根据不同类型的产品显示显示销售价格'''
      
        for line in self:
            if line.ponderable:
                line.sale_price = "%s/g" % line.real_time_price_unit
            else:
                line.sale_price = "%s/件" % line.list_price
    @api.model
    def create(self, vals):
        attribute_value_ids = vals.get('attribute_value_ids',[])
        material = 0
        style = 0
        model = 0
        norms_list = []
        if attribute_value_ids:
            attribute_value_ids = attribute_value_ids[0][2]
            value_objs = self.env['product.attribute.value'].search([('id','in',attribute_value_ids)])
            for line in value_objs:
                if line.attribute_id.code == 'material':
                    material = line.sequence
                elif line.attribute_id.code == 'style':
                    style = line.sequence
                elif line.attribute_id.code == 'model':
                    model = line.sequence
                else:
                    norms_list.append(line.sequence)
            norms_list.sort()
            suffix = ''
            for i in range(len(norms_list)):
                suffix = "%s%s" % (suffix,norms_list[i])
            default_code = "%s%s-%s-%s" %(material,style,model,suffix)
            vals['default_code'] = default_code
            
        return super(prdouct_product,self).create(vals)
    @api.multi
    def _compute_attribute(self):
        '''获得某个类别的实时单价'''
        #默认为0
        for product in self:
            product.standard_weight = 0
            product.real_time_price_unit = 0
            #为可称量产品
            if product.ponderable:
                attribute_value_ids = product.attribute_value_ids
                for line in attribute_value_ids:
                    if line.attribute_id.code == "material":
                        materail_price = self.env['product.attribute.material.price'].\
                        search([('attribute_value_id','=',line.id),('attribute_id','=',line.attribute_id.id),('active','=',True)])
                        product.real_time_price_unit = materail_price.price_unit
                    if line.attribute_id.code == "weight":       
                        m= re.match(r"(^[0-9]\d*\.\d|\d+)", line.name) 
                        weight = m.group(1)
                        product.standard_weight = float(weight)


            