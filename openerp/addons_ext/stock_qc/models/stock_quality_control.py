# -*- coding: utf-8 -*-
'''
Created on 2016年3月11日

@author: cloudy
'''
from openerp import models,fields


class stock_quality_control(models.Model):
    _name = "stock.quality.control"
    
    QC_RESULT = [
        ('passed', 'Passed'),
        ('partial', 'Partial Passed'),
        ('rejected', 'Rejected'),
    ]
    name = fields.Char(string='Reference')
    partner_id = fields.Many2one('res.partner',string='res partner')
    purchase_id = fields.Many2one('purchase.order',string='purchase order')
    qc_result = fields.Selection(QC_RESULT,string='qc result', help="""
            * Passed: all products passed.\n
            * Partial Passed: Some products have a problem.\n
            * Rejected: all products have a problem.\n
            """)
    qc_date =fields.Datetime(string='DC Datetime')
    qc_note = fields.Text(string='QC Notes')
    qc_checker = fields.Many2one('res.users',string='QC Checker')
    location_id = fields.Many2one('stock.location')
    
    
    
    
    