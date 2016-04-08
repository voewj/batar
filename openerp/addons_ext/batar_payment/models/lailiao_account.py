# -*- coding: utf-8 -*-
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

class Lailiao_order(models.Model):
    _name = 'batar.lailiao'

    name = fields.Char(string='名称', required=True, default='New')
    description = fields.Text(string='摘要')
    partner_id = fields.Many2one('res.partner', string='客户', readonly=True, states={'draft': [('readonly', 'False')]})
    credit = fields.Float(string="欠", readonly=True, states={'draft': [('readonly', 'False')]}, digits=dp.get_precision('Lai liao'))
    debit = fields.Float(string="存", readonly=True, states={'draft': [('readonly', 'False')]}, digits=dp.get_precision('Lai liao'))
    weight = fields.Float(string="原重量", readonly=True, states={'draft': [('readonly', 'False')]}, digits=dp.get_precision('Lai liao'))
    assay = fields.Float(string="成色", readonly=True, states={'draft': [('readonly', 'False')]})
    sale_id = fields.Many2one('sale.order', string="关联单号", readonly=True, states={'draft': [('readonly', 'False')]})
    state = fields.Selection([('draft', '草稿'), ('done', '完成')], default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('lailiao') or "New"
            res = super(Lailiao_order, self).create(vals)
            return  res