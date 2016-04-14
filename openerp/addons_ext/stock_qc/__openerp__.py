# -*- coding: utf-8 -*-
{
    'name': "stock_qc",

    'summary': """
        质检模块""",

    'description': """
        入库之前质量检测
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase','product_info_extend'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/purchase_order.xml',
        'views/stock_warehouse.xml',
        'views/stock_qc.xml',
      
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}