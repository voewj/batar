# -*- coding: utf-8 -*-
from openerp import http

# class StockSplitDisplay(http.Controller):
#     @http.route('/stock_split_display/stock_split_display/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_split_display/stock_split_display/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_split_display.listing', {
#             'root': '/stock_split_display/stock_split_display',
#             'objects': http.request.env['stock_split_display.stock_split_display'].search([]),
#         })

#     @http.route('/stock_split_display/stock_split_display/objects/<model("stock_split_display.stock_split_display"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_split_display.object', {
#             'object': obj
#         })