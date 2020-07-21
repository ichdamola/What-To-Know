# -*- coding: utf-8 -*-

import time
import odoo.addons.decimal_precision as dp
from odoo import models, fields, api, _
from odoo.exceptions import Warning

class PrepaymentWriteoff(models.Model):
    _name = 'loan.prepayment.writeoff'
    _description = 'Loan Prepayment WriteOff'
    _inherit = ['mail.thread']
    
    @api.multi
    def onchange_prepayment(self, loan_id=False):
        res = {}
        res['value'] = {'gross_value': 0.0, 'value_residual': 0.0, 'name':''}
        if not loan_id:
            return res
        prepayment_obj = self.env['employee.loan.details']
        if loan_id:
            prepayment = prepayment_obj.browse(loan_id)
            res['value'].update({
                'purchase_value': prepayment.final_total,
                'total_repaid': prepayment.total_amount_paid,
                'value_residual': prepayment.total_amount_due,
                'name': prepayment.name,
                'account_prepayment_id': prepayment.employee_loan_account.id,
            })
        return res
    
    @api.multi
    def validate(self):
        for cap in self:
            pass
            cap.state = 'open'
#         return self.write({'state': 'open'})
    
    @api.multi
    def approve(self):
        for cap in self:
            pass
#            if cap.prepayment_id.state in ('draft', 'close'):
#                raise osv.except_osv(_('Error !'),_("You can not approve writeoff of prepayment when related prepayment is in Draft/Close state."))
            cap.state = 'approve'
#         return self.write({'state': 'approve'})
    
    @api.multi
    def set_to_draft_app(self):
        for rec in self:
            rec.state = 'draft'
#         return self.write({'state': 'draft'})
    
    @api.multi
    def set_to_draft(self):
        for rec in self:
            rec.state = 'draft'
#         return self.write({'state': 'draft'})
    
    @api.multi
    def set_to_close(self):
        for rec in self:
            rec.state = 'reject'
#         return self.write({'state': 'reject'})
    
    @api.multi
    def set_to_cancel(self):
        for rec in self:
            rec.state = 'cancel'
#         return self.write({'state': 'cancel'})

    @api.multi
    def create_move_write(self):
#         period_obj = self.env['account.period']
        move_obj = self.env['account.move']
        move_line_obj = self.env['account.move.line']
        created_move_ids = []
        for line in self:
#            for d in line.prepayment_id.depreciation_line_ids:
#                if d.move_id and d.move_id.state=='draft':
#                    raise osv.except_osv(_('Error !'),_('You can not approve writeoff of prepayment because There are unposted Journals relating this prepayment. Either post or cancel them.'))
            if not line.write_journal_id or not line.write_account:
                raise Warning(_('Accounting information missing, please check write off account and write off journal'))
            if line.state == 'done':
                raise Warning(_('Accounting Moves already created.'))
            if line.state != 'approve':
                raise Warning(_('Can not create write offs entry in current state.'))
#             period_ids = period_obj.find(line.date)
            company_currency = line.loan_id.company_id.currency_id
            current_currency = line.loan_id.company_id.currency_id  # line.loan_id.currency_id.id
            ctx = dict(self._context or {})
            ctx.update({'date': line.date})
            amount = current_currency.compute(line.value_residual, company_currency)
            if line.write_journal_id.type == 'purchase':
                sign = 1
            else:
                sign = -1
            prepayment_name = 'Write offs ' + line.loan_id.name
            reference = line.name
            move_vals = {
                'date': line.date,
                'ref': reference,
#                 'period_id': period_ids and period_ids.id or False,
                'journal_id': line.write_journal_id.id,
            }
            move_id = move_obj.create(move_vals)
            journal_id = line.write_journal_id.id
            address_id = line.loan_id.employee_id.address_home_id or False
            partner_id = address_id and address_id and address_id.id or False
#            partner_id = line.prepayment_id.partner_id.id
            debit_line = (0, 0, {
                'name': prepayment_name,
                'ref': reference,
                'move_id': move_id.id,
                'account_id': line.write_account.id,
                'debit': line.value_residual,
                'credit': 0.0,
#                 'period_id': period_ids and period_ids.id or False,
                'journal_id': journal_id,
                'partner_id': partner_id,
                'currency_id': company_currency.id <> current_currency.id and current_currency.id or False,
                'amount_currency': company_currency.id <> current_currency.id and -sign * line.value_residual or 0.0,
                'date': line.date,
                'company_id': line.company_id.id
            })
            credit_line = (0, 0, {
                'name': prepayment_name,
                'ref': reference,
                'move_id': move_id.id,
                'account_id': line.account_prepayment_id.id,
                'credit': line.value_residual,
                'debit': 0.0,
#                 'period_id': period_ids and period_ids.id or False,
                'journal_id': journal_id,
                'partner_id': partner_id,
                'currency_id': company_currency.id <> current_currency.id and current_currency.id or False,
                'amount_currency': company_currency.id <> current_currency.id and sign * line.value_residual or 0.0,
                'date': line.date,
                'company_id': line.company_id.id
#                'prepayment_id': line.prepayment_id.id
            })
            
#             move_line_obj.create({
#                 'name': prepayment_name,
#                 'ref': reference,
#                 'move_id': move_id.id,
#                 'account_id': line.write_account.id,
#                 'debit': line.value_residual,
#                 'credit': 0.0,
# #                 'period_id': period_ids and period_ids.id or False,
#                 'journal_id': journal_id,
#                 'partner_id': partner_id,
#                 'currency_id': company_currency.id <> current_currency.id and current_currency.id or False,
#                 'amount_currency': company_currency.id <> current_currency.id and -sign * line.value_residual or 0.0,
#                 'date': line.date,
#             })
#             move_line_obj.create({
#                 'name': prepayment_name,
#                 'ref': reference,
#                 'move_id': move_id.id,
#                 'account_id': line.account_prepayment_id.id,
#                 'credit': line.value_residual,
#                 'debit': 0.0,
# #                 'period_id': period_ids and period_ids.id or False,
#                 'journal_id': journal_id,
#                 'partner_id': partner_id,
#                 'currency_id': company_currency.id <> current_currency.id and current_currency.id or False,
#                 'amount_currency': company_currency.id <> current_currency.id and sign * line.value_residual or 0.0,
# #                'analytic_account_id': line.prepayment_id.category_id.account_analytic_id.id,
#                 'date': line.date,
# #                'prepayment_id': line.prepayment_id.id
#             })
            move_id.update({'line_ids': [debit_line, credit_line]})
            created_move_ids.append(move_id.id)
            line.write({'move_id1': move_id.id})
            line.write({'state': 'done'})
            line.loan_id.write({'state':'paid'})
        return True
    
    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default.update({'state':'draft', 'move_id1': False})
        return super(PrepaymentWriteoff, self).copy(default)

    write_account = fields.Many2one(
        'account.account', 
        string='Write off Account', 
        required=False, 
        readonly=False, 
        states={'done':[('readonly', True)]}
    )              
    write_journal_id = fields.Many2one(
        'account.journal', 
        string='Write off Journal', 
        required=False, 
        readonly=False, 
        states={'done':[('readonly', True)]}
    )
    
    name = fields.Char(
        string='Name', 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    move_id1 = fields.Many2one(
        'account.move', 
        string='Journal Entry', 
        readonly=True
    )
    emp_id = fields.Many2one(
        'hr.employee', 
        string='Employee', 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    loan_id = fields.Many2one(
        'employee.loan.details', 
        string='Loan', 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    account_prepayment_id = fields.Many2one(
        'account.account', 
        string='Employee Loan Account', 
        required=False, 
        readonly=False, 
        states={'done':[('readonly', True)]}
    )
    writeoff_value = fields.Float(
        string='Writeoff Amount ', 
        digits=dp.get_precision('Account'), 
        required=False, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    purchase_value = fields.Float(
        string='Original Value ', 
        digits=dp.get_precision('Account'), 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    total_repaid = fields.Float(
        string='Total Repaid ', 
        digits=dp.get_precision('Account'), 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )     
    value_residual = fields.Float(
        string='Closing Balance', 
        digits=dp.get_precision('Account'), 
        readonly=True, 
        states={'draft':[('readonly', False)]}
    )
    user_id = fields.Many2one(
        'res.users', 
        string='Responsible User', 
        required=False, 
        readonly=True, 
        states={'draft':[('readonly', False)]}, 
        default=lambda self:self.env.user
    )
    company_id = fields.Many2one(
        'res.company', 
        string='Company', 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}, 
        default=lambda self:self.env.user.company_id
    )
    date = fields.Date(
        string='Date', 
        required=True, 
        readonly=True, 
        states={'draft':[('readonly', False)]}, 
        default=time.strftime('%Y-%m-%d')
    )
#        'recompute_prepayment': fields.boolean('Recompute',readonly=False, states={'approve':[('readonly',True)],'reject':[('readonly',True)], 'cancel':[('readonly',True)]}, help='Tick if you want to upDate the gross value of prepayment and recompute the depreciation with new gross value.'),
    state = fields.Selection(
        selection=[('draft', 'New'), 
        ('open', 'Confirmed'), 
        ('approve', 'Approved'), 
        ('done', 'Done'),
        ('reject', 'Rejected'), 
        ('cancel', 'Cancelled')], 
        string='State', 
        required=True,
        help="When an writeoff is created, the state is 'New'.\n" \
        "If the writeoff is confirmed, the state goes in 'Confirmed' \n" \
        "If the writeoff is approved, the state goes in 'Approved' \n" \
        "If the writeoff is done, the state goes in 'Done' \n" \
        "If the writeoff is rejected, the state goes in 'Rejected' \n" \
        "If the writeoff is cancelled, the state goes in 'Cancelled' \n" \
        ,readonly=True, 
        default='draft',
        track_visibility='onchange',
    )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
