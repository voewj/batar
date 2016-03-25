# -*- coding: utf-8 -*-
'''
Created on 2016年3月25日

@author: cloudy
'''

from openerp import http
import json
from ..common import *

class OpenApi(http.Controller):
    
    @http.route(['/api'],type='http',auth='public',methods=['POST','GET'])
    def base_api(self,**kwargs):
        print 'request'
        print 'kwargs',kwargs
        response_data = {
            'code':'500',
            'data':{}
        }
        return http.Response(json.dumps(response_data,ensure_ascii=False))