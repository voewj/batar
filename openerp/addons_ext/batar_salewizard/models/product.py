# -*- coding:utf-8 -*-
from openerp import api, fields, models
from openerp import api, tools, SUPERUSER_ID

#class Batar_product(models.Model):
#    _inherit = 'product.product'


 #   def name_get(self, cr, user, ids, context=None):

"""
把属性值按属性的序列号来排序，统一产品系列名字格式
"""
#            attribute_value = product.attribute_value_ids.sorted(lambda r: r.attribute_id.sequence)


class Product_attribute(models.Model):
    _inherit = 'product.attribute.value'
    """
    修改属性值排序方式，按属性值对应的属性ID来排序，统一产品系列的名字格式
    """
    _order = 'attribute_id'

    sequence = fields.Integer(readonly=True)