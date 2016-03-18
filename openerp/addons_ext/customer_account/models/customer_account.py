# -*- coding: utf-8 -*-
'''
Created on 2016年3月15日

@author: cloudy
'''
from openerp import models,fields,api

class customer_account_type(models.Model):
    _name = 'customer.account.type'
    
    name = fields.Char(string='customer account type')
    
class customer_account(models.Model):
    _name = 'customer.account'
    
    partner_id = fields.Many2one('res.partner',string='customer')
    record_type = fields.Many2one('customer.account.type',string='customer account type')
    user_id = fields.Many2one('res.users',string='record person')
    category_id = fields.Many2one('product.category',string='product category')
    weight = fields.Float(string='product weight')
    amount_money = fields.Float(string='amount of money')
    sale_id = fields.Many2one('sale.order',string='sale orrder')
    picking_id = fields.Many2one('stock.picking',string='stock picking')
    account_id = fields.Many2one('account.invoice',string='account invoice')
    interest_rate_money = fields.Float(string='interest rate money')
    interest_rate_stock = fields.Float(string='interest rate stock')
    user_comment = fields.Text(string='user comment')
    expenses_id = fields.Many2many('customer.account',string='expenses records')
    expenses_comment = fields.Text(string='expenses comment')
    account_clean = fields.Boolean(string='account clean')
    
    
