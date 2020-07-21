# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'
    _description = 'account.payment'
    
    @api.multi
    def post(self):
        res = super(AccountPayment, self).post()
        #todo: check the if amount is less then installment amount then it could not be applicable to pay installment
        for payment in self:
            if payment.installment:
                payment.installment.write({'state': 'paid'})
        return res
    
    installment = fields.Many2one(
        'loan.installment.details', 
        string='Loan Installment', 
        readonly=False, 
        copy=False,
        states={'draft':[('readonly',False)]}
    )
 # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:   
