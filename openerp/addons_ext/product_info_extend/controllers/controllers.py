# -*- coding: utf-8 -*-
from openerp import http

# class ProductInfoExtend(http.Controller):
#     @http.route('/product_info_extend/product_info_extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_info_extend/product_info_extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_info_extend.listing', {
#             'root': '/product_info_extend/product_info_extend',
#             'objects': http.request.env['product_info_extend.product_info_extend'].search([]),
#         })

#     @http.route('/product_info_extend/product_info_extend/objects/<model("product_info_extend.product_info_extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_info_extend.object', {
#             'object': obj
#         })