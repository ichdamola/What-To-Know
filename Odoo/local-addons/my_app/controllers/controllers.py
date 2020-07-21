# -*- coding: utf-8 -*-
from odoo import http

# class Local-addons/myApp(http.Controller):
#     @http.route('/local-addons/my_app/local-addons/my_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/local-addons/my_app/local-addons/my_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('local-addons/my_app.listing', {
#             'root': '/local-addons/my_app/local-addons/my_app',
#             'objects': http.request.env['local-addons/my_app.local-addons/my_app'].search([]),
#         })

#     @http.route('/local-addons/my_app/local-addons/my_app/objects/<model("local-addons/my_app.local-addons/my_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('local-addons/my_app.object', {
#             'object': obj
#         })