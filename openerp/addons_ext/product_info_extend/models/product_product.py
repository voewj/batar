# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models

class prdouct_product(models.Model):
    _inherit = "product.product"
    

    standard_weight = fields.Float(related='product_tmpl_id.standard_weight',store=True,string="Standard Weight")
    item_fee = fields.Float(related='product_tmpl_id.item_fee',store=True,string="Item Fee")
    ponderable = fields.Boolean(related='product_tmpl_id.ponderable',store=True,string='ponderable')
    

    _defaults = {
        'type': "product",
        'ponderable':True,
    }
    
# class sale_config_settings(models.Model):
#     _inherit = 'sale.config.settings'
#     
#     defaults = {
#         'group_product_variant':1,#产品可以有多个属性
#         #fixed: 每产品单一售价
#         #percentage: 每客户段不同售价
#         #formula: 基于公式的高级定价 
#         'sale_pricelist_setting':'percentage',
#         #0: 销售订单不加运输成本
#         #1: 允许追加送货成本 
#         'module_delivery':1,
#         #0: 产品只有一个计量单位
#         #1: 一些产品可使用不同的单位销售 / 采购 ( 高级 ) 
#         'group_uom':1,
#         }