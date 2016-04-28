# -*- coding: utf-8 -*-
{
    'name': "需要模块一键安装",

    'summary': """
    需要模块一键安装
        """,

    'description': """
        为了免去每次部署手动安装多个模块的麻烦，采取依赖的方式一键安装所有需要的模块。
        如果需要新增模块，直接在此模块中添加依赖
    """,

    'author': "cloudy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant','crm','sale','purchase','product','stock','board','l10n_cn','l10n_cn_standard',
                'account_voucher','account_cancel','account_budget',
                'fetchmail','crm_partner_assign','crm_claim','product_email_template','mail','delivery','sale_order_dates',
                'product_menu','customer_extend','customer_import','sale_order_extend','product_info_extend',
                'procurement_order','product_import','stock_extend','stock_import',
                'multi_warehouse_management','recycling_warehouse','stock_split_display','stock_qc',
                'purchase_extend','customer_info_extend','batar_salewizard','batar_product_expense','batar_payment','batar_product_cart',
                'batar_bi',
#                 'account_extend',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'base_config/base_init.xml',
        'base_config/product_initial_data.xml',
        'base_config/stock_init.xml',
       
       
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}