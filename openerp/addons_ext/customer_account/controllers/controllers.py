# -*- coding: utf-8 -*-
from openerp import http

# class CustomerAccount(http.Controller):
#     @http.route('/customer_account/customer_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_account/customer_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_account.listing', {
#             'root': '/customer_account/customer_account',
#             'objects': http.request.env['customer_account.customer_account'].search([]),
#         })

#     @http.route('/customer_account/customer_account/objects/<model("customer_account.customer_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_account.object', {
#             'object': obj
#         })