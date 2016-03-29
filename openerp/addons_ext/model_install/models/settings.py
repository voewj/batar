# -*- coding: utf-8 -*-

from openerp.osv import  osv

class stock_config_settings(osv.osv_memory):
    _inherit = 'stock.config.settings'
    _defaults = {
        'group_stock_inventory_valuation':1
    }