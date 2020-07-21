from odoo import models, fields 
from odoo.addons import decimal_precision as dp



class EmployeeLoanDetails(models.Model):
	_inherit = 'employee.loan.details'

	plots = fields.Integer('Number of Plots')
	# active = fields.Boolean("Active", default=True)
	proof = fields.Binary(string='Proof',attachment=True)