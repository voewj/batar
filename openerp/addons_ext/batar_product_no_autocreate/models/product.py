# -*- coding:utf-8 -*-
from openerp import api, fields, models, _

class ProductCategory(models.Model):
    _inherit = 'product.category'

    no_create_variants = fields.Boolean(
        string="Don't create variants automatically",
        help='This check disables the automatic creation of product variants '
             'for all the products of this category.', default=True)

    @api.multi
    @api.onchange('no_create_variants')
    def onchange_no_create_variants(self):
        self.ensure_one()
        if not self._origin:
            return {}
        return {'warning': {'title': _('Change warning!'),
                            'message': _('Changing this parameter may cause'
                                         ' automatic variants creation')}}

    @api.multi
    def write(self, values):
        res = super(ProductCategory, self).write(values)
        if ('no_create_variants' in values and
                not values.get('no_create_variants')):
            self.env['product.template'].search(
                [('categ_id', '=', self.id),
                 ('no_create_variants', '=', 'empty')]).create_variant_ids()
        return res


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    variants_create_auto = fields.Selection(
        [('yes', 'Create Auto'),
         ('no', "Don't create Auto"),
         ('category', 'use the category value')
         ], required=True, string="Create Auto", default='no')


    @api.multi
    @api.onchange('variants_create_auto')
    def onchange_no_create_variants(self):
        self.ensure_one()
        if not self._origin:
            return {}
        return {'warning': {'title': _('Change warning!'),
                            'message': _('Changing this parameter may cause'
                                         ' automatic variants creation')}}

    @api.multi
    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        if 'variants_create_auto' in values:
            self.create_variant_ids()
        return res
    @api.multi
    def create_variant_ids(self):
        for tmpl in self:
            if ((tmpl.variants_create_auto == 'empty' and
                    not tmpl.categ_id.no_create_variants) or
                    (tmpl.variants_create_auto == 'yes')):
                return super(ProductTemplate, self).create_variant_ids()
            else:
                return True

class Product(models.Model):

    _inherit = 'product.product'


    @api.onchange('product_tmpl_id')
    def product_tmpl_values_onchange(self):
        if self.product_tmpl_id:
            values = self.env['product.attribute.value']
            attribute_line = self.env['product.attribute.line'].search([('product_tmpl_id', '=', self.product_tmpl_id.id)])
            for i in attribute_line:
                values += i.value_ids
            return {'domain': {'attribute_value_ids': [('id', 'in', values.ids)]}}
        else:
            return {'domain': {'attribute_value_ids': [('id', 'in', [])]}}
    #
    # attribute_value_ids = fields.Many2many(domain=product_tmpl_values_onchange)

    # product_tmpl_values = fields.Many2many('product.attribute.value', id1='value_id', id2='tmpl')
    # @api.multi
    # @api.onchange('product_tmpl_id')
    # def onchange_product_tmpl(self):
    #     context = self._context or {}
    #     self.ensure_one()
    #     if self.product_tmpl_id:
    #         values = self.env['product.attribute.value']
    #         attribute_line = self.env['product.attribute.line'].search(
    #             [('product_tmpl_id', '=', self.product_tmpl_id.id)])
    #         for i in attribute_line:
    #             values += i.value_ids
    #         print values
    #         # self.product_tmpl_values = values
    #         self._context['domain_ids']=values.ids


