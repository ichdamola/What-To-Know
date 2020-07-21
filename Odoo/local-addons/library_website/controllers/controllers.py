# -*- coding: utf-8 -*-
from odoo import http

# class Local-addons/libraryWebsite(http.Controller):
#     @http.route('/local-addons/library_website/local-addons/library_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/local-addons/library_website/local-addons/library_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('local-addons/library_website.listing', {
#             'root': '/local-addons/library_website/local-addons/library_website',
#             'objects': http.request.env['local-addons/library_website.local-addons/library_website'].search([]),
#         })

#     @http.route('/local-addons/library_website/local-addons/library_website/objects/<model("local-addons/library_website.local-addons/library_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('local-addons/library_website.object', {
#             'object': obj
#         })