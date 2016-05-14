# -*- coding: utf-8 -*-
'''
Created on 2016年2月25日

@author: cloudy
'''
from openerp import fields,models,api
from openerp.tools.common_ext import GetNextSequence

# import openerp.addons.decimal_precision as dp

class product_template(models.Model):
    _inherit = "product.template"
    
    ponderable = fields.Boolean(string='ponderable')
    sequence = fields.Integer(string='sequence',default=1)
    
    _defaults = {
        'type': "product",
        'ponderable':True,
        'categ_id':2,
    }
    @api.model
    def create(self, vals):
        templateObj = self.env['product.template'].search([],limit=1,order='id desc')
        sequence = 1
        if templateObj:
            sequence = GetNextSequence(sequence)
        vals['sequence'] = sequence
        return super(product_template,self).create(vals)
    
    

        