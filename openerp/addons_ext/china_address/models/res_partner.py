# -*- coding: utf-8 -*-
'''
Created on 2016年3月11日

@author: cloudy
'''

from openerp import fields,models

class res_partner(models.Model):
    _inherit = 'res.partner'
    
    district_id = fields.Many2one('res.country.state.city.district',string='district')
    city_id = fields.Many2one(related='district_id.city_id',string='city')
    province_id = fields.Many2one(realted="district_id.province_id",string='province')
    
    
    
