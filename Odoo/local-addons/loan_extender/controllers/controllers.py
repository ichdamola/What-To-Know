# -*- coding: utf-8 -*-
from odoo import http

# class LoanExtender(http.Controller):
#     @http.route('/loan_extender/loan_extender/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loan_extender/loan_extender/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loan_extender.listing', {
#             'root': '/loan_extender/loan_extender',
#             'objects': http.request.env['loan_extender.loan_extender'].search([]),
#         })

#     @http.route('/loan_extender/loan_extender/objects/<model("loan_extender.loan_extender"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loan_extender.object', {
#             'object': obj
#         })