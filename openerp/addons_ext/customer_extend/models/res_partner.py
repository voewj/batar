# -*- coding: utf-8 -*-
'''
Created on 2016年1月15日

@author: cloudy
'''

from openerp import fields, models 

class res_partner(models.Model):
    _inherit = 'res.partner'
    
    _credit_level = [
        ('diamond',"Diamond customer"),
        ('platinum',"Platinum customers"),
        ('white_gold',"White Gold customers"),
        ('gold',"Gold customers"),
        ('silver',"Silver customers"),
        ('ordinary',"Ordinary customers"),
    ]
    customer_code = fields.Char(size=50,string='Customer Code')
    credit_line = fields.One2many('res.partner.credit.line','partner_id',string="Customer Credit Limit")
    credit_level = fields.Selection(_credit_level,string='credit level')
    
    _defaults = {
        'credit_level':'ordinary',
    }

class res_partner_credit_line(models.Model):
    _name = 'res.partner.credit.line'
    
    partner_id = fields.Many2one('res.partner',string='Customer',ondelete='cascade')
    credit_category_id = fields.Many2one("res.partner.credit.category", string="Credit Category")
    value = fields.Float(string="Credit Category Value")
    
     
class res_partner_credit_category(models.Model):
    _name = "res.partner.credit.category"
    name = fields.Char(String="Credit Category")