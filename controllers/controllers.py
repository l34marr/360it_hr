# -*- coding: utf-8 -*-
# from odoo import http


# class 360itHr(http.Controller):
#     @http.route('/360it_hr/360it_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/360it_hr/360it_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('360it_hr.listing', {
#             'root': '/360it_hr/360it_hr',
#             'objects': http.request.env['360it_hr.360it_hr'].search([]),
#         })

#     @http.route('/360it_hr/360it_hr/objects/<model("360it_hr.360it_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('360it_hr.object', {
#             'object': obj
#         })
