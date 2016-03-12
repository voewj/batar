# -*- coding: utf-8 -*-
from openerp import http

# class StockQc(http.Controller):
#     @http.route('/stock_qc/stock_qc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_qc/stock_qc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_qc.listing', {
#             'root': '/stock_qc/stock_qc',
#             'objects': http.request.env['stock_qc.stock_qc'].search([]),
#         })

#     @http.route('/stock_qc/stock_qc/objects/<model("stock_qc.stock_qc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_qc.object', {
#             'object': obj
#         })