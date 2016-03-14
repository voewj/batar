# -*- coding: utf-8 -*-
from openerp import http

# class PageModify(http.Controller):
#     @http.route('/page_modify/page_modify/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/page_modify/page_modify/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('page_modify.listing', {
#             'root': '/page_modify/page_modify',
#             'objects': http.request.env['page_modify.page_modify'].search([]),
#         })

#     @http.route('/page_modify/page_modify/objects/<model("page_modify.page_modify"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('page_modify.object', {
#             'object': obj
#         })