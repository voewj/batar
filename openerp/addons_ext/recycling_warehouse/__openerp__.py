# -*- coding: utf-8 -*-
{
    'name': "recycling_warehouse",

    'summary': """
        收料仓""",

    'description': """
       回收客户的旧料
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/recycling_product.xml',
        'data/recycling_warehouse.xml',
        'views/recycling_warehouse.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}