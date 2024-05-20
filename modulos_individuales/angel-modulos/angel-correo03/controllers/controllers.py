# -*- coding: utf-8 -*-
# from odoo import http


# class Angel-correo03(http.Controller):
#     @http.route('/angel-correo03/angel-correo03', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/angel-correo03/angel-correo03/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('angel-correo03.listing', {
#             'root': '/angel-correo03/angel-correo03',
#             'objects': http.request.env['angel-correo03.angel-correo03'].search([]),
#         })

#     @http.route('/angel-correo03/angel-correo03/objects/<model("angel-correo03.angel-correo03"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('angel-correo03.object', {
#             'object': obj
#         })
