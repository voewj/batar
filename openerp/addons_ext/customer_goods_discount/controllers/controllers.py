# -*- coding: utf-8 -*-
from openerp import http

# class CustomerGoodsDiscount(http.Controller):
#     @http.route('/customer_goods_discount/customer_goods_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_goods_discount/customer_goods_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_goods_discount.listing', {
#             'root': '/customer_goods_discount/customer_goods_discount',
#             'objects': http.request.env['customer_goods_discount.customer_goods_discount'].search([]),
#         })

#     @http.route('/customer_goods_discount/customer_goods_discount/objects/<model("customer_goods_discount.customer_goods_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_goods_discount.object', {
#             'object': obj
#         })