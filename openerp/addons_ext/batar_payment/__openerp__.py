# -*- coding: utf-8 -*-
{
    'name': '尚金缘存欠支付',
    'author': 'Xiao',
    'description': """
    统计客户存欠信息。以客户存欠信息抵扣销售收款。
    """,
    'depends': ['base', 'account', 'product', 'sale'],
    'data': [
        'views/batar_lailiao_view.xml',
        'views/partner_view.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
    ],
    'application': True,

}