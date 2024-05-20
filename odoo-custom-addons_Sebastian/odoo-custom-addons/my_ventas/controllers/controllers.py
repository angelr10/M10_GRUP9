# -*- coding: utf-8 -*-

from odoo import http


class MyVentas(http.Controller):
    @http.route('/my_ventas/my_ventas', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_ventas/my_ventas/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_ventas.listing', {
            'root': '/my_ventas/my_ventas',
            'objects': http.request.env['my_ventas.my_ventas'].search([]),
        })

    @http.route('/my_ventas/my_ventas/objects/<model("my_ventas.my_ventas"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_ventas.object', {
            'object': obj
        })
