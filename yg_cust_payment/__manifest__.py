# -*- coding: utf-8 -*-
{
    'name': "YG Customer Payment Report",

    'summary': """
            Interview Tasks
        """,

    'description': """
        Customer Payment PDF Report
        Menu is added under Invoicing -> Reporting -> Customer Payment Report
    """,

    'author': "Ajaykrishnap",
    'website': "https://www.yougotagift.com",
    'category': 'Accounting/Accounting',
    'version': '16.0.1.0.',
    'depends': ['account','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/customer_payment_wizard_views.xml',
        'report/customer_payment_report.xml'
    ],
    'application': True

}
