# -*- coding: utf-8 -*-
'''
Created on 2016年3月16日
增加支付方式 account.payment由account.abstract.payment继承而来
@author: cloudy
'''

from openerp import models,fields

class account_payment(models.Model):
    _inherit = 'account.payment'
    
    journal_id = fields.Many2one('account.journal', string='Payment Method', required=True, domain=[('type', 'in', ('bank', 'cash','gold'))])
