# -*- coding: utf-8 -*-
from openerp import http

# class ProductMenu(http.Controller):
#     @http.route('/product_menu/product_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_menu/product_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_menu.listing', {
#             'root': '/product_menu/product_menu',
#             'objects': http.request.env['product_menu.product_menu'].search([]),
#         })

#     @http.route('/product_menu/product_menu/objects/<model("product_menu.product_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_menu.object', {
#             'object': obj
#         })