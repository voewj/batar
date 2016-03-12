# -*- coding: utf-8 -*-
from openerp import http

# class QualityInspection(http.Controller):
#     @http.route('/quality_inspection/quality_inspection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quality_inspection/quality_inspection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quality_inspection.listing', {
#             'root': '/quality_inspection/quality_inspection',
#             'objects': http.request.env['quality_inspection.quality_inspection'].search([]),
#         })

#     @http.route('/quality_inspection/quality_inspection/objects/<model("quality_inspection.quality_inspection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quality_inspection.object', {
#             'object': obj
#         })