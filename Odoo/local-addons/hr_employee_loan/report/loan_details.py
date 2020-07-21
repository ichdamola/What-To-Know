# -*- coding: utf-8 -*-


import time
from odoo import api, models, _
from odoo.exceptions import UserError
# from openerp.report import report_sxw
# 
# class loan_details(report_sxw.rml_parse):
#     def __init__(self, cr, uid, name, context=None):
#         super(loan_details, self).__init__(cr, uid, name, context=context)
#         self.localcontext.update({
#             'get_lines':self._get_lines
#         })

class loan_details(models.AbstractModel):
    _name = 'report.hr_employee_loan.loan_report_analysis_qweb'
    
    def _get_lines(self, lines):
        res = []
        count = 1
        for line in lines:
            access = 0.0
            temp = {}
#             print line.install_no
            if count == 1 or line.install_no == 1:
                open_amt = line.loan_id.principal_amount
            temp['no'] = line.install_no
            temp['emi'] = line.total
            temp['principal'] = line.principal_amt
            temp['opening_bal'] = open_amt
            temp['interest'] = line.interest_amt
            access = round(line.total - (line.principal_amt + line.interest_amt), 2)
            temp['closing_bal'] = round(open_amt - line.principal_amt - access, 2)
            temp['state'] = line.state
            temp['date_from'] = line.date_from
            temp['date_to'] = line.date_to
            if temp['closing_bal'] < 0:temp['closing_bal'] = 0.0
            open_amt = temp['closing_bal']
            res.append(temp)
            count = count + 1 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>res>>>>>",res)
        return res
    
    
    @api.model
    def get_report_values(self, docids, data=None):
        print('data=================',self.env.context)
        self.model = self.env.context.get('active_model')
        print('self.model-------------',self.model)
        docs = self.env[self.model].browse(self.env.context.get('active_ids', []))
#         display_account = data['form'].get('display_account')
        lines = self.env['employee.loan.details'].search([])
#         get_lines = self.with_context(data['form'].get('used_context'))._get_lines(lines)
 
        return {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'Lines': get_lines,
        }
        
        

#         self.model = self.env.context.get('active_model')
#         docs = self.env[self.model].browse(self.env.context.get('active_ids', []))
#         display_account = data['form'].get('display_account')
#         accounts = docs if self.model == 'account.account' else self.env['account.account'].search([])
#         account_res = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
# 
#         return {
#             'doc_ids': self.ids,
#             'doc_model': self.model,
#             'data': data['form'],
#             'docs': docs,
#             'time': time,
#             'Accounts': account_res,
#         }
        
# class report_test(osv.AbstractModel):
#     _name = "report.hr_employee_loan.loan_report_analysis_qweb"
#     _inherit = "report.abstract_report"
#     _template = "hr_employee_loan.loan_report_analysis_qweb"
#     _wrapped_report_class = loan_details

#report_sxw.report_sxw('report.loan.details', 'employee.loan.details', 'addons/ng_loan_payroll/report/loan_details.rml', parser=loan_details)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

