# -*- coding: utf-8 -*-
'''
Created on 2016年2月23日

@author: cloudy
'''
from openerp import http

class ApiApp(http.Controller):
    @http.route('/openapi/order/',methods=('POST','GET'),auth='public')
    def api_app(self,**kw):
        print 'enter ========================================='
        return '12312'