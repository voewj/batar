# -*- coding: utf-8 -*-
{
    'name': "实时金价",

    'summary': """
                实时金价，订单价格计算时需要从此模块获得金价""",

    'description': """
                实时金价，订单价格计算时需要从此模块获得金价
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_category.xml',
        'views/product_price_real_time.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}