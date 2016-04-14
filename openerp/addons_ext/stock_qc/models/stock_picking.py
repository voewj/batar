# -*- coding: utf-8 -*-
'''
Created on 2016年3月23日

@author: cloudy
'''
from openerp import models,fields,_
from openerp.exceptions import UserError


class stock_picking_type(models.Model):
    _inherit = 'stock.picking.type'
    
    is_quality = fields.Boolean(related='warehouse_id.is_quality',string='is quality stock warehouse')

class stock_quality_picking(models.Model):
    _inherit= 'stock.picking'
    
    QC_RESULT = [
        ('passed','passed'),
        ('partial','partial passed'),
        ('rejected','rejected'),
    ]
    
    is_quality = fields.Boolean(related='picking_type_id.is_quality',string='is quality stock warehouse')
    qc_result = fields.Selection(QC_RESULT,string='quality check result')
    qc_date = fields.Datetime(string='quality check date time')
    qc_note = fields.Text(string='quality check note')
    qc_checker = fields.Many2one('res.users',string='quality checker')
    
    _defaults = {
        'qc_result':"passed",
       
    }
    def do_new_transfer(self, cr, uid, ids, context=None):
        """"""
        pack_op_obj = self.pool['stock.pack.operation']
        data_obj = self.pool['ir.model.data']
        for pick in self.browse(cr, uid, ids, context=context):
            location_id = pick.location_dest_id
            to_delete = []
            if not pick.move_lines and not pick.pack_operation_ids:
                raise UserError(_('Please create some Initial Demand or Mark as Todo and create some Operations. '))
            # In draft or with no pack operations edited yet, ask if we can just do everything
            if pick.state == 'draft' or all([x.qty_done == 0.0 for x in pick.pack_operation_ids]):
                # If no lots when needed, raise error
                picking_type = pick.picking_type_id
                if (picking_type.use_create_lots or picking_type.use_existing_lots):
                    for pack in pick.pack_operation_ids:
                        if pack.product_id and pack.product_id.tracking != 'none':
                            raise UserError(_('Some products require lots, so you need to specify those first!'))
                view = data_obj.xmlid_to_res_id(cr, uid, 'stock.view_immediate_transfer')
                wiz_id = self.pool['stock.immediate.transfer'].create(cr, uid, {'pick_id': pick.id}, context=context)
                return {
                     'name': _('Immediate Transfer?'),
                     'type': 'ir.actions.act_window',
                     'view_type': 'form',
                     'view_mode': 'form',
                     'res_model': 'stock.immediate.transfer',
                     'views': [(view, 'form')],
                     'view_id': view,
                     'target': 'new',
                     'res_id': wiz_id,
                     'context': context,
                 }

            # Check backorder should check for other barcodes
            if self.check_backorder(cr, uid, pick, context=context):
                view = data_obj.xmlid_to_res_id(cr, uid, 'stock.view_backorder_confirmation')
                wiz_id = self.pool['stock.backorder.confirmation'].create(cr, uid, {'pick_id': pick.id}, context=context)
                return {
                         'name': _('Create Backorder?'),
                         'type': 'ir.actions.act_window',
                         'view_type': 'form',
                         'view_mode': 'form',
                         'res_model': 'stock.backorder.confirmation',
                         'views': [(view, 'form')],
                         'view_id': view,
                         'target': 'new',
                         'res_id': wiz_id,
                         'context': context,
                     }
            for operation in pick.pack_operation_ids:
                if operation.qty_done < 0:
                    raise UserError(_('No negative quantities allowed'))
                if operation.qty_done > 0:
                    pack_op_obj.write(cr, uid, operation.id, {'product_qty': operation.qty_done}, context=context)
                else:
                    to_delete.append(operation.id)
            if to_delete:
                pack_op_obj.unlink(cr, uid, to_delete, context=context)
        self.do_transfer(cr, uid, ids, context=context)
        return
        
    
    
    
    