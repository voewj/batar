# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteSaleExtend(http.Controller):
#     @http.route('/website_sale_extend/website_sale_extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_extend/website_sale_extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_extend.listing', {
#             'root': '/website_sale_extend/website_sale_extend',
#             'objects': http.request.env['website_sale_extend.website_sale_extend'].search([]),
#         })

#     @http.route('/website_sale_extend/website_sale_extend/objects/<model("website_sale_extend.website_sale_extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_extend.object', {
#             'object': obj
#         })