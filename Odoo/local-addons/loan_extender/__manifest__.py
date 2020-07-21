# -*- coding: utf-8 -*-
{
    'name': "loan_extender",

    'summary': """
        Extends the loan module.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "DataTotems",
    'website': "https://www.datatotems.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1',
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_employee_loan'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #'report/loan_report_inherit.xml',
        'report/loan_report_inherit_template.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}