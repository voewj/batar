# -*- coding: utf-8 -*-
{
    'name': "客户改进",

    'summary': """
        客户资料信息改进""",

    'description': """
        Long description of module's purpose
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/credit_category.xml',
        'data/customer_category.xml',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}