# -*- coding: utf-8 -*-
'''
Created on 2016年3月31日

@author: cloudy
'''
from openerp import models,fields,api,_
from openerp.exceptions import UserError


class stock_pack_operation(models.Model):
    _inherit = 'stock.pack.operation'
    
    QC_RESULT = [
        ('passed','passed'),
        ('partial','partial passed'),
        ('rejected','rejected'),
    ]
    
    qc_result = fields.Selection(QC_RESULT,string='quality check result')
    pass_qty = fields.Float(string='pass qty')
    all_stand_weight = fields.Float(string='all stand weight')
    receive_weight = fields.Float(string='receive weight')
    back_qty = fields.Float(compute='_get_back_qty',string='back qty')
    back_weight = fields.Float(string='back weight')
    
    @api.multi
    def _get_back_qty(self):
        for line in self:
            line.back_qty = line.product_qty-line.pass_qty
    @api.model
    def create(self, vals):
        product_qty = vals.get('product_qty',0)
        product_id = vals.get('product_id',None)
        if product_id:
            product= self.env['product.product'].search([('id','=',product_id)])
            if product:
                all_stand_weight = product_qty * product.standard_weight
                vals['all_stand_weight'] = all_stand_weight
        vals['pass_qty'] = product_qty
        return super(stock_pack_operation,self).create(vals)
    
    _defaults = {
        'qc_result':"passed",
    }
    
    
    @api.onchange('pass_qty','back_weight')
    def quality_check_change(self):
        if self.receive_weight < self.back_weight:
            raise UserError(_('back weight must less than receive weight'))
        
        pass_qty = int(self.pass_qty)
        product_qty = int(self.product_qty)
        if product_qty < pass_qty:
            raise UserError(_('pass qty must less than product qty'))
        if pass_qty < product_qty:
            
            self.qc_result = 'partial'
        else:
            self.qc_result ="passed"
        if pass_qty < 1:
            self.qc_result = 'rejected'
        if self.qc_result != 'passed':
            self.picking_id.qc_result = 'partial'
          
        self.qty_done = self.pass_qty
        self.back_qty = self.product_qty - self.pass_qty
        
        self.write({
            "qc_result":self.qc_result
        })

            
                