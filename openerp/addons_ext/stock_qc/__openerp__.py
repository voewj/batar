# -*- coding: utf-8 -*-
{
    'name': "stock_qc",

    'summary': """
        质量控制""",

    'description': """
       质量控制
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/qc_security.xml',
        'views/stock_qc.xml',
      
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}