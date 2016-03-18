# -*- coding: utf-8 -*-
'''
Created on 2016年3月16日

@author: cloudy
'''

from openerp import models,fields

class account_jouranl(models.Model):
    _inherit = 'account.journal'
    type = fields.Selection([
            ('sale', 'Sale'),
            ('purchase', 'Purchase'),
            ('cash', 'Cash'),
            ('bank', 'Bank'),
            ('general', 'Miscellaneous'),
            ('gold','Gold'),
        ], required=True,
        help="Select 'Sale' for customer invoices journals."\
        " Select 'Purchase' for vendor bills journals."\
        " Select 'Cash' or 'Bank' for journals that are used in customer or vendor payments."\
        " Select 'General' for miscellaneous operations journals."\
        " Select 'Opening/Closing Situation' for entries generated for new fiscal years.")
