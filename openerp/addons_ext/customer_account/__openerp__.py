# -*- coding: utf-8 -*-
{
    'name': "customer_account",

    'summary': """
        客户账户信息""",

    'description': """
        客户账户信息
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/customer_account.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}