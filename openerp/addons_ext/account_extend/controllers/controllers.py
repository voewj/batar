# -*- coding: utf-8 -*-
from openerp import http

# class AccountExtend(http.Controller):
#     @http.route('/account_extend/account_extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_extend/account_extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_extend.listing', {
#             'root': '/account_extend/account_extend',
#             'objects': http.request.env['account_extend.account_extend'].search([]),
#         })

#     @http.route('/account_extend/account_extend/objects/<model("account_extend.account_extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_extend.object', {
#             'object': obj
#         })