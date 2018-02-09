# -*- coding: utf-8 -*-
from odoo import http

# class Ccrm(http.Controller):
#     @http.route('/ccrm/ccrm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ccrm/ccrm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ccrm.listing', {
#             'root': '/ccrm/ccrm',
#             'objects': http.request.env['ccrm.ccrm'].search([]),
#         })

#     @http.route('/ccrm/ccrm/objects/<model("ccrm.ccrm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ccrm.object', {
#             'object': obj
#         })