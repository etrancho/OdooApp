# -*- coding: utf-8 -*-
# from odoo import http


# class Regalos(http.Controller):
#     @http.route('/regalos/regalos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/regalos/regalos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('regalos.listing', {
#             'root': '/regalos/regalos',
#             'objects': http.request.env['regalos.regalos'].search([]),
#         })

#     @http.route('/regalos/regalos/objects/<model("regalos.regalos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('regalos.object', {
#             'object': obj
#         })
