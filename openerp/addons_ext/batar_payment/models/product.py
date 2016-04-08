# -*- coding: utf-8 -*-
from openerp import fields, api, models

class Batar_product(models.Model):
    _inherit = 'product.template'

    process_cost = fields.Float(string="基础工费", help="每个产品的基本加工费用！")