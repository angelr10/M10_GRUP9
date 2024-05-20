# -*- coding: utf-8 -*-
from odoo import http


class CrmJuno(http.Controller):
    @http.route('/crm_juno/crm_juno', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/crm_juno/crm_juno/objects', auth='public')
    def list(self, **kw):
        return http.request.render('crm_juno.listing', {
            'root': '/crm_juno/crm_juno',
            'objects': http.request.env['crm_juno.crm_juno'].search([]),
        })

    @http.route('/crm_juno/crm_juno/objects/<model("crm_juno.crm_juno"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('crm_juno.object', {
            'object': obj
        })
