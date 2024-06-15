# -*- coding: utf-8 -*-
{
    'name': 'YG Purchase Dashboard',
    'version': '16.0.1.0.0',
    'category': 'Purchase',
    'summary': 'Dashboard for Purchase',
    'description': """This module is developed for displaying the count of 
    purchase orders, total amount for purchase orders and total 
    untaxed amount for purchase orders.""",
    'author': "Ajaykrishnap",
    'website': "https://www.yougotagift.com",
    'depends': [
        'base',
        'purchase'
    ],
    'data': [
            'views/purchase_order_views.xml',
             ],
    'assets': {
        'web.assets_backend': [
            'yg_purchase_dashboard/static/src/xml/*.xml',
            'yg_purchase_dashboard/static/src/js/*.js',
        ],
    },
    'application': False,
}
