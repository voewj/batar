# -*- coding: utf-8 -*-
from openerp import http

# class DatePrice(http.Controller):
#     @http.route('/date_price/date_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/date_price/date_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('date_price.listing', {
#             'root': '/date_price/date_price',
#             'objects': http.request.env['date_price.date_price'].search([]),
#         })

#     @http.route('/date_price/date_price/objects/<model("date_price.date_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('date_price.object', {
#             'object': obj
#         })