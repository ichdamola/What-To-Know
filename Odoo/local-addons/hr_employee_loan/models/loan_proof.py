# -*- coding: utf-8 -*-

from odoo import models, fields

class LoanProof(models.Model):
    _name = 'loan.proof'
    _description = "Loan Proof"
    
    name = fields.Char(
        string='Name',
        required=True,
    )
    mandatory = fields.Boolean(
        string='Mandatory'
    )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: