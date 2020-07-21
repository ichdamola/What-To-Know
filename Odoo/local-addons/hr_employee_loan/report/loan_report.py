# -*- coding: utf-8 -*-

import time

from openerp.osv import osv
from openerp.report import report_sxw

class loan_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(loan_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_loan': self._get_loan_ids,
            'get_total':self._get_total,
            'get_total_received':self._get_total_received,
            'get_total_due':self._get_total_due,
        })
        self.loan_ids = []

    def _get_total(self):
        total = 0.0
        for loan in self.loan_ids:
            total += loan.final_total
        return total
    
    def _get_total_received(self):
        total = 0.0
        for loan in self.loan_ids:
            total += loan.total_amount_paid
        return total

    def _get_total_due(self):
        total = 0.0
        for loan in self.loan_ids:
            total += loan.total_amount_due
        return total

    def _get_loan_ids(self, data):
        field_dict ={'principal':'principal_amount',
                     'state':'state',
                     'applied':'date_approved',
                     'approved':'date_applied',
                     'rejected':'date_repayment',
                     'loan_type':'loan_type'
                     }
        dom = []
        if data['filter'] in ('applied','approved','rejected'):
            if data['condition'] == 'range':
                dom += [(field_dict[data['filter']], '>=', data['date1']),(field_dict[data['filter']], '<=', data['date2'])]
            else:
                dom += [(field_dict[data['filter']],'%s'%(data['condition']), data['date1'])]
        elif data['filter'] == 'principal':
            if data['condition'] == 'range':
                dom += [(field_dict[data['filter']], '>=', data['amount1']),(field_dict[data['filter']], '<=', data['amount2'])]
            else:
                dom += [(field_dict[data['filter']],'%s'%(data['condition']), data['amount1'])]
        elif data['filter'] == 'loan_type':
            dom += [(field_dict[data['filter']], '=', data['loan_type'][0])]
        else:
            dom += [(field_dict[data['filter']], '=', data['state'])]
        if data['employee_ids']:
            dom+=[('employee_id', 'in', data['employee_ids'])]
#         result_loan_ids = self.pool.get('employee.loan.details').search(self.cr, self.uid, dom)
#         self.loan_ids = self.pool.get('employee.loan.details').browse(self.cr, self.uid, result_loan_ids)

        result_loan_ids = self.env['employee.loan.details'].search(dom)
#         print result_loan_ids
        self.loan_ids = result_loan_ids#self.pool.get('employee.loan.details').browse(self.cr, self.uid, result_loan_ids)
#         print 'result_loan_ids------------------>',result_loan_ids
        return self.loan_ids 
    
class report_test(osv.AbstractModel):
    _name = "report.hr_employee_loan.loan_report_from_wiz"
    _inherit = "report.abstract_report"
    _template = "hr_employee_loan.loan_report_from_wiz"
    _wrapped_report_class = loan_report

#report_sxw.report_sxw('report.loan.report', 'employee.loan.details', 'addons/ng_loan_payroll/report/loan_report.rml', parser=loan_report)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

