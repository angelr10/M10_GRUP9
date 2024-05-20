# -*- coding: utf-8 -*-
from odoo import http


class MyFacturacion(http.Controller):
    @http.route('/my_facturacion/my_facturacion', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_facturacion/my_facturacion/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_facturacion.listing', {
            'root': '/my_facturacion/my_facturacion',
            'objects': http.request.env['my_facturacion.my_facturacion'].search([]),
        })

    @http.route('/my_facturacion/my_facturacion/objects/<model("my_facturacion.my_facturacion"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_facturacion.object', {
            'object': obj
        })
