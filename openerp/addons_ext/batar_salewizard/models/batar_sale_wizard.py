# -*- coding:utf-8 -*-
from openerp import api, fields, models, exceptions
import logging
_logger = logging.getLogger(__name__)

class Sale_orderWiard(models.TransientModel):
    _name = 'batar.sale.wizard'

    product_id = fields.Many2one('product.template', string='Product template')
    sale_line = fields.Many2many('sale.order.line', string='Added Product')
    test = fields.Integer(string="Test", default=1)
    attribute_value_ids = fields.Many2many('product.attribute.value', string='Arribute value')

    @api.onchange('product_id')
    def attribute_value_onchange(self):
        if self.product_id:
            attribute = self.product_id.attribute_line_ids
            value = []
            for a in attribute:
                value.extend(a.value_ids.ids)
            self.attribute_value_ids = self.env['product.attribute.value'].search([('id', 'in', value)])


    @api.multi
    def reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'context': self._context,
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
    @api.multi
    def confirm(self):
        self.ensure_one()
        return True
    @api.multi
    def cancel(self):
        self.ensure_one()
        if self.sale_line:
            self.sale_line.unlink()
        return True
    @api.model
    def _count(self):
        return len(self._context.get('active_ids', []))

    @api.multi
    def confirm_attribute(self):
        self.ensure_one()
        if not self.product_id:
            raise exceptions.ValidationError('no product template！')
#        elif self.sale_line:
#            if self.sale_line[0].product_id.product_tmpl_id == self.product_id:
#                raise exceptions.ValidationError('已添加该类产品！')
        else:
            values = self.attribute_value_ids.ids
            products = self.env['product.product'].search([('product_tmpl_id', '=', self.product_id.id)])
            line_ids = []
            for p in products:
                attribute = p.attribute_value_ids.ids
                same_attribute = [a for a in attribute if a in values]
                tmp = list(set(attribute) - set(same_attribute))
                if len(tmp) == 0:
                    order_line = self.env['sale.order.line']
                    sale_obj = self.env['sale.order']
                    order = sale_obj.browse(self._context.get('active_ids'))[0]
                    name = p.name_get()[0][1]
                    if p.description_sale:
                        name += '\n' + p.description_sale
                    line_id = order_line.create({'product_id': p.id,
                                                 'order_id': order.id,
                                                 'name': name,
                                                 'price_unit': 0.0,
                                                 'product_uom_qty': 1.0,
                                                 'product_uom': p.uom_id.id,

                                                 })
                    line_ids.append(line_id.id)
            self.sale_line = self.env['sale.order.line'].search([('id', 'in', line_ids)])
        return self.reopen_form()




