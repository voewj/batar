# -*- coding: utf-8 -*-
'''
Created on 2016年3月25日

@author: cloudy
'''
import urllib
import urllib2

def httpPost(url='',params={}):
    '''http请求数据'''
    params = urllib.urlencode(params)
    response = urllib.urlopen(url, params)
    result = ''
    try:
        result = response.read()
    finally:
        return result



 