# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api
# import openerp.addons.decimal_precision as dp

class product_template(models.Model):
    _inherit = "product.template"
    
    standard_weight = fields.Float(string="Standard Weight")
    item_fee = fields.Float(string="Item Fee")
    ponderable = fields.Boolean(string='ponderable')
    real_time_price_unit = fields.Float(compute='_get_real_time_price_unit',string='real time price unit')
    

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    @api.one
    @api.depends('categ_id')
    def _get_sub_top_category(self):
        '''获得之类顶级类别'''
        
        category_id = self.categ_id
        sub_top_category = None
        while True:
            if category_id.sub_top:
                sub_top_category = category_id
                break
            else:
                category_id = category_id.parent_id
        return sub_top_category
        
    @api.one
    @api.depends('categ_id')
    def _get_real_time_price_unit(self):
        '''获得某个类别的实时单价'''
        sub_top_category = self._get_sub_top_category()
        if isinstance(sub_top_category,list):
            sub_top_category = sub_top_category[0]
        if sub_top_category is None:
            self.real_time_price_unit = 0
        else:
            objs = self.env['product.price.real.time'].search([('category_id','=',sub_top_category.id),('active','=',True)])
            if objs:
                objs.sorted()
                objs = objs[0]
                self.real_time_price_unit = objs.real_time_price_unit
            else:
                self.real_time_price_unit = 0
        
        
        
        