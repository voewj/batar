# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api

class prdouct_product(models.Model):
    _inherit = "product.product"
    

    standard_weight = fields.Float(compute='_compute_attribute',store=True,string="Standard Weight")
    item_fee = fields.Float(related='product_tmpl_id.item_fee',store=True,string="Item Fee")
    weight_fee = fields.Float(related='product_tmpl_id.weight_fee',store=True,string="weight fee")
    ponderable = fields.Boolean(related='product_tmpl_id.ponderable',store=True,string='ponderable')
    real_time_price_unit = fields.Float(compute='_compute_attribute',string='real time price unit')
    shang_code = fields.Char(string='show king code')
    

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    @api.multi
    def _compute_attribute(self):
        '''获得某个类别的实时单价'''
        #默认为0
        self.real_time_price_unit = 0
        self.standard_weight = 0
        #为可称量产品
        if self.ponderable:
            attribute_value_ids = self.attribute_value_ids
            for line in attribute_value_ids:
                if line.attribute_id.code == "M":
                    materail_price = self.env['product.attribute.material.price'].\
                    search([('attribute_value_id','=',line.id),('attribute_id','=',line.attribute_id.id),('active','=',True)])
                    self.real_time_price_unit = materail_price.price_unit
       











            