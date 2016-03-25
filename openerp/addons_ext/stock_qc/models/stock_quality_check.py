# -*- coding: utf-8 -*-
'''
Created on 2016年3月23日

@author: cloudy
'''
from openerp import models,fields


class stock_quality_check(models.Model):
    inherit= 'stock.picking'
    _name = 'stock.quality.check'
    
    