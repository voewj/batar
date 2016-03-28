# -*- coding: utf-8 -*-
'''
Created on 2016年3月23日

@author: cloudy
'''
from openerp import models,fields

class stock_location(models.Model):
    _inherit = 'stock.location'
    
    qc_location = fields.Boolean(string='is quality check stock picking')
    _defaults = {
        'qc_location':False,
    }


class stock_quality_picking(models.Model):
    _inherit= 'stock.picking'
    
    QC_RESULT = [
        ('passed','passed'),
        ('partial','partial passed'),
        ('rejected','rejected'),
    ]
    
    qc_result = fields.Selection(QC_RESULT,string='quality check result')
    qc_date = fields.Datetime(string='quality check date time')
    qc_note = fields.Text(string='quality check note')
    qc_checker = fields.Many2one('res.users',string='quality checker')
    _defaults = {
        'qc_result':"passed",
        
    }
    
    
    
    