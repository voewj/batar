# -*- coding: utf-8 -*-
'''
Created on 2016年3月7日

@author: cloudy
'''
from openerp import fields,models

class account_customer_category(models.Model):
    _name = 'account.customer.category'
    name = fields.Char(string='account customer category')
class account_customer(models.Model):
    _name = 'account.customer'
    
    partner_id = fields.Many2one('res.partner',string='customer')
    account_line = fields.One2many('account.customer.line')

class account_customer_line(models.Model):
    _name= 'account.customer.line'
    
    account_customer_id = fields.Many2one('account.customer','account_line',string='account customer')
    category_id = fields.Many2one('account.customer.category',string='account customer category')
    
    
    
