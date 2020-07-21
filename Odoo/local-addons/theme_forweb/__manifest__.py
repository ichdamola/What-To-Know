# -*- coding: utf-8 -*-
{
  'name':'Loan theme',
  'description': 'This is the theme for the loan website',
  'version':'1.0',
  'author':'Ifedayo',

  'data': ['static/src/xml/signup.xml',
  			# 'views/signup.xml',
  			'templates/assets.xml',
  			'views/new.xml',
            'security/ir.model.access.csv'
  ],
  'qweb': [
        'static/src/xml/signup.xml',
        ],
  'category': 'Theme/Creative',
  'depends': ['website', 'website_theme_install','hr_employee_loan'],
}