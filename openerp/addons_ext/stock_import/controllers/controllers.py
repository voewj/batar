# -*- coding: utf-8 -*-
from openerp import http

# class StockImport(http.Controller):
#     @http.route('/stock_import/stock_import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_import/stock_import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_import.listing', {
#             'root': '/stock_import/stock_import',
#             'objects': http.request.env['stock_import.stock_import'].search([]),
#         })

#     @http.route('/stock_import/stock_import/objects/<model("stock_import.stock_import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_import.object', {
#             'object': obj
#         })