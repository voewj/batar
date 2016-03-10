# -*- coding: utf-8 -*-
from openerp import http

# class ModelInstall(http.Controller):
#     @http.route('/model_install/model_install/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/model_install/model_install/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('model_install.listing', {
#             'root': '/model_install/model_install',
#             'objects': http.request.env['model_install.model_install'].search([]),
#         })

#     @http.route('/model_install/model_install/objects/<model("model_install.model_install"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('model_install.object', {
#             'object': obj
#         })