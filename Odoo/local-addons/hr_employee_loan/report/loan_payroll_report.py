# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api, _

MONTHS = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
]

class LoanAnalysisReport(models.Model):
    """ Loan Analysis """
    _name = "loan.analysis.report"
    _auto = False
    _description = "Loan Analysis"
    _rec_name = 'loan_day'

    loan_year = fields.Char(string='Loan Year', readonly=True, help="Loan year")
    loan_month = fields.Selection(selection=MONTHS, string='Loan Month', readonly=True, help="Loan month")
    loan_day = fields.Char(string='Loan Day', readonly=True, help="Loan day")
    employee_id = fields.Many2one('hr.employee', string='Employee')
    date_applied = fields.Date(string='Date Applied')
    date_approved = fields.Date(string='Date Approved')
    date_repayment = fields.Date(string='Date Of Repayment')
    duration = fields.Integer(string='Duration(months)')
    interest_mode = fields.Selection(selection=[('flat', 'Flat'), ('reducing', 'Reducing')], string='Interest Mode')
    principal_amount = fields.Float(string='Principal Amt.', digits=(16, 2))
    final_total = fields.Float(string='Total', digits=(16, 2))
    total_amount_paid = fields.Float(string='Received', digits=(16, 2))
    total_amount_due = fields.Float(string='Residual', digits=(16, 2))
    total_interest_amount = fields.Float(string='Interest', digits=(16, 2))
    max_loan_amt = fields.Float(string='Max Loan Amount', digits=(16, 2))
    state = fields.Selection(selection=[
       ('draft', 'Draft'),
       ('applied', 'Applied'),
       ('approved', 'Approved'),
       ('paid', 'Paid'),
       ('disburse', 'Disbursed'),
       ('rejected', 'Rejected'),
       ('cancel', 'Cancelled')], string='State')
    
    @api.model_cr
    def init(self):

        """
            Loan Analysis Report
            @param cr: the current row, from the database cursor
        """
        tools.drop_view_if_exists(self.env.cr, 'loan_analysis_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW loan_analysis_report AS (
                SELECT
                    id,
                    to_char(l.date_approved, 'YYYY') as loan_year,
                    to_char(l.date_approved, 'MM') as loan_month,
                    to_char(l.date_approved, 'YYYY-MM-DD') as loan_day,
                    
                    l.date_approved as date_approved,
                    l.date_applied as date_applied,
                    l.date_repayment as date_repayment,
                    l.state as state,
                    l.employee_id as employee_id,
                    l.duration as duration,
                    l.interest_mode as interest_mode,
                    l.principal_amount as principal_amount,
                    l.final_total as final_total,
                    l.total_amount_paid as total_amount_paid,
                    l.total_amount_due as total_amount_due,
                    l.total_interest_amount as total_interest_amount,
                    l.max_loan_amt as max_loan_amt
                FROM
                    employee_loan_details l 
                group by
                    l.id,
                    l.date_approved,
                    l.date_applied,
                    l.date_repayment,
                    l.state,
                    l.employee_id ,
                    l.duration,
                    l.interest_mode,
                    l.principal_amount ,
                    l.final_total ,
                    l.total_amount_paid ,
                    l.total_amount_due ,
                    l.total_interest_amount ,
                    l.max_loan_amt
            )""")

 # (SELECT id from loan_policy WHERE 
  #                      id = (SELECT id from policy_employee_rel
   #                         WHERE employee_id = l.employee_id))  as policy_ids
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
