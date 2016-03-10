# -*- coding: utf-8 -*-
'''
Created on 2016年3月8日

@author: cloudy
'''
from openerp import models,fields,_


class product_template(models.Model):
    _inherit = 'product.template'
    
    percentage =fields.Float(string='percentage')
    
    def _get_product_template_type(self, cr, uid, context=None):
        res = super(product_template, self)._get_product_template_type(cr, uid, context=context)
        if 'recycling' not in [item[0] for item in res]:
            res.append(('recycling', _('Recycling Product')))
        return res
    
