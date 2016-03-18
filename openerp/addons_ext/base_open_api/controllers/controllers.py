# -*- coding: utf-8 -*-
from openerp import http

# class BaseOpenApi(http.Controller):
#     @http.route('/base_open_api/base_open_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_open_api/base_open_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_open_api.listing', {
#             'root': '/base_open_api/base_open_api',
#             'objects': http.request.env['base_open_api.base_open_api'].search([]),
#         })

#     @http.route('/base_open_api/base_open_api/objects/<model("base_open_api.base_open_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_open_api.object', {
#             'object': obj
#         })