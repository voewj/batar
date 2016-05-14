# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api,_
from openerp.exceptions import UserError
import re


class product_template(models.Model):
    _inherit = 'product.template'

    name = fields.Char(translate=False)


class prdouct_product(models.Model):
    _inherit = "product.product"
    

    standard_weight = fields.Float(compute='_compute_attribute',string="Standard Weight")
    item_fee = fields.Float(string="Item Fee")
    weight_fee = fields.Float(string="weight fee")
    additional_fee = fields.Float(string='additional fee') 
    ponderable = fields.Boolean(related='product_tmpl_id.ponderable',store=True,string='ponderable')
    real_time_price_unit = fields.Float(compute='_compute_attribute',string='real time price unit')
    sale_price = fields.Char(compute='_compute_sale_price',string='display sale price')
    

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    _sql_constraints = [
        ('default_uniq', 'unique(default_code)', 'default_code must be unique!'),
    ]
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
        product_tmpl_id = vals.get('product_tmpl_id',None)
        if not product_tmpl_id:
            raise UserError(_("Must set the product template before create product")) 
        tmplObj = self.env['product.template'].search([('id','=',product_tmpl_id)])
        attribute_value_ids = vals.get('attribute_value_ids',[])

        #下面3个list用于生成编码
        firstCode =None
        SecondCode = {}
        thirdCode=''
        default_code=''
        if attribute_value_ids:
            material=self.env['ir.model.data'].get_object_reference('product_info_extend', 'product_attribute_material')[1]
            attribute_value_ids = attribute_value_ids[0][2]
            value_objs = self.env['product.attribute.value'].search([('id','in',attribute_value_ids)])
            for line in value_objs:
                if line.attribute_id.code == 'material':
                    firstCode = line.sequence
                elif line.attribute_id.code == 'weight':
                    m = re.match(r"(^[0-9]\d*\.\d|\d+)",line.name)
                    thirdCode =  m.group(1)
                else:
                    SecondCode[line.attribute_id.name] = "%s" % line.sequence
                    
            if firstCode is None:
                raise UserError(_("Must set the material of the product")) 
            default_code = "%s0%s" % (firstCode,tmplObj.sequence)
            if SecondCode:
                
                SecondCodeStr = "0".join([SecondCode[v] for v in sorted(SecondCode.keys())])
                default_code = "%s-%s"%(default_code,SecondCodeStr)
            if thirdCode:
                default_code = "%s-%s"%(default_code,thirdCode)
            vals['default_code'] = default_code
        else:
            raise UserError(_("Must set the properties of the product")) 
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


            