# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class EmpLoanReport(models.TransientModel):
    _name = 'emp.loan.report'
    _description = 'Employees Loan Report'

    employee_ids = fields.Many2many(
        'hr.employee', 
        'emp_loan_rel', 
        'employee_id', 
        'report_id', 
        string='Employees'
    )
    loan_type = fields.Many2one(
        'loan.type', 
        string='Loan Type'
    )
    filter = fields.Selection(selection=[
        ('applied','Applied Date'),
        ('approved','Approved Date'),
        ('rejected','Repayment Date'),
        ('loan_type','Loan Type'),
        ('state','State'),
        ('principal','Principal Amount')], 
        string='Filter On', 
        required=True,
#       comment by probuse  select=True, 
        default='applied'
    )
    date1 = fields.Date(
        string='Date 1'
    )
    date2 = fields.Date(
        string='Date 2'
    )
    amount1 =fields.Float(
        string='Amount 1', 
        digits=(16,2)
    )
    amount2 =fields.Float(
        'Amount 2', 
        digits=(16,2)
    )
    condition = fields.Selection(selection=[
       ('<','Less than'),
       ('>','Greater than'),
       ('<=','Less than equal to'),
       ('>=','Greater than equal to'),
       ('range','Between'),
       ('=','Equal to')], string='Condition',
#     comment by probuse   select=True, 
       defalt='='
    )
    state = fields.Selection(selection=[
       ('draft','Draft'),
       ('applied','Applied'),
       ('approved','Approved'),
       ('paid','Paid'),
       ('rejected','Rejected'),
       ('cancel','Cancelled')], 
       string='State',
# comment by probuse                              select=True
    )
    
    @api.multi
    def print_report(self, data):
        wiz_rec = self.read()
        data.update(form=wiz_rec[0],ids=self.ids)
#        return {
#            'type': 'ir.actions.report.xml',
#            'report_name': 'loan.report',
#            'datas': data,
#        }
        return self.env['report'].get_action(self, 'hr_employee_loan.loan_report_from_wiz', data)#self.pool['report'].get_action(self._cr, self._uid, [], 'ng_loan_payroll.loan_report_from_wiz', data=data)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: