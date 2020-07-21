# -*- coding: utf-8 -*-

from odoo import models, fields

class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    is_loan_payment = fields.Boolean(
        string='Loan Payment',
    )
