# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ThemeForweb(http.Controller):
	@http.route(['/signup'], type='http', auth='public', website=True)
	def signup_form(self, **post):
		return request.render("theme_forweb.signup_form", {})

	@http.route(['/signup/submit'], type='http', auth='public', website=True)
	def signup_form_submit(self, **post):

		""" This function originally written by Ifedayo creates all the listed fields of the employee model-hr.employee
		and prints them in the server, thats the get method. It is then rendered in the template id below."""

		employee = request.env['hr.employee'].create({

			#Contact Information
			'name' : post.get('name'),
			# 'image': post.get('image'),
			'emergency_contact' : post.get('emergency_contact'),
			'emergency_phone' : post.get('emergency_phone'),
			'home_id' : post.get('home_id'),

			#Birth

			'birthday' : post.get('birthday'),
			'place_of_birth' : post.get('place_of_birth'),
			'birth_country' : post.get('birth_country'),

			# #Education

			'certificate_level' : post.get('certificate_level'),
			'study_field' : post.get('study_field'),
			'study_school' : post.get('study_school'),

			# #Status

			'genders' : post.get('genders'),
			'marital_status' : post.get('marital_status'),
			'children' : post.get('children'),

			# #Citizenship and other info

			'country_ids' : post.get('country_ids'),
			'identification_id' : post.get('identification_id'),
			'passport_id' : post.get('passport_id'),
			'bank_account_ids' : post.get('bank_account_ids'),
			'bank_name' : post.get('bank_name'),
			'account_name': post.get('account_name'),

			# #Work information

			'address_ids' : post.get('address_ids'),
			'work_location' : post.get('work_location'),
			'work_email' : post.get('work_email'),
			'mobile_phone' : post.get('mobile_phone'),
			'work_phone' : post.get('work_phone'),

			# #Position

			# # 'department_id' : post.get('department_id'),
			# # 'job_id' : post.get('job_id'),
			# 'job_title' : post.get('job_title'),
			# # 'category_id' : post.get('category_id'),

		})
		# user = request.env['res.users'].create({'login' : post.get("login")})

		vals = {
			'employee' : employee,
		}
		return request.render("theme_forweb.signup_form_success", vals)






		# user = request.env['res.users'].create({
		# 	'name' : post.get('name'),
 	# 		'new_password' : post.get('new_password'),
 	# 		'email': post.get('email'),
 	# 		'login': post.get('email')
		# })





#     @http.route('/theme_forweb/theme_forweb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_forweb/theme_forweb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_forweb.listing', {
#             'root': '/theme_forweb/theme_forweb',
#             'objects': http.request.env['theme_forweb.theme_forweb'].search([]),
#         })

#     @http.route('/theme_forweb/theme_forweb/objects/<model("theme_forweb.theme_forweb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_forweb.object', {
#             'object': obj
#         })

