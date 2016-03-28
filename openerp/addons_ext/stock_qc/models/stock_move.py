# -*- coding: utf-8 -*-
'''
Created on 2016年3月25日

@author: cloudy
'''
from openerp import models,fields

class stock_move(models.Model):
    _inherit = 'stock.move'
    
    
    QC_RESULT = [
        ('passed','passed'),
        ('partial','partial passed'),
        ('rejected','rejected'),
    ]
    qc_result = fields.Selection(QC_RESULT,string='quality check result')
    
    _defaults = {
        'qc_result':"passed",
    }
    