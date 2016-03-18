# -*- coding: utf-8 -*-

'''
Created on 2016年3月18日

@author: cloudy
'''
from openerp import models,fields


class open_api_authentication(models.Model):
    _name = 'open.api.authentication'
    
    user_id = fields.Many2one('res.users',string='res users')
    active = fields.Boolean(string='active')
    app_key = fields.Char(string='app key')
    key_secret =fields.Char(string='key secret')
    period = fields.Datetime(string='validity period') 
    _sql_constraints = [
        ('app_key_uniq', 'unique(app_key)', 'app_key must be unique!'),
        ('key_secret_uniq', 'unique(key_secret)', 'key_secret must be unique!'),
    ]

    