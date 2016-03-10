# -*- coding: utf-8 -*-
from openerp import http

# class AccountCustomer(http.Controller):
#     @http.route('/account_customer/account_customer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_customer/account_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_customer.listing', {
#             'root': '/account_customer/account_customer',
#             'objects': http.request.env['account_customer.account_customer'].search([]),
#         })

#     @http.route('/account_customer/account_customer/objects/<model("account_customer.account_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_customer.object', {
#             'object': obj
#         })