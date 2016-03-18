# -*- coding: utf-8 -*-
{
    'name': "account_extend",

    'summary': """
        财务扩展，用于支持黄金抵价""",

    'description': """
          财务扩展，用于支持黄金抵价
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/account_journal_initial.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}