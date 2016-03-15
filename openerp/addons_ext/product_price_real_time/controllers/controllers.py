# -*- coding: utf-8 -*-
from openerp import http

# class ProductPriceRealTime(http.Controller):
#     @http.route('/product_price_real_time/product_price_real_time/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_price_real_time/product_price_real_time/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_price_real_time.listing', {
#             'root': '/product_price_real_time/product_price_real_time',
#             'objects': http.request.env['product_price_real_time.product_price_real_time'].search([]),
#         })

#     @http.route('/product_price_real_time/product_price_real_time/objects/<model("product_price_real_time.product_price_real_time"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_price_real_time.object', {
#             'object': obj
#         })