# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_juno(models.Model):
    _name = 'crm_juno.crm_juno'
    _description = 'crm_juno.crm_juno'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class crmjunocustomer(models.Model):
    _name = 'crm.juno.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    orders = fields.One2many('crm.juno.order', 'customer_id', string='Orders')
    client_type = fields.Selection([('individual', 'Individual'), ('company', 'Company')], string='Client Type', default='individual')

    @api.model
    def create_customer(self, name, orders, email=None, phone=None, address=None, client_type='individual'):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'client_type': client_type,
        }
        customer = self.env['crm.juno.customer'].create(vals)
        if orders:
            order_vals_list = [(0, 0, order) for order in orders]
            customer.orders = order_vals_list
        return customer

class crmjunoorder(models.Model):
    _name = 'crm.juno.order'
    _description = 'Order'

    name = fields.Char(string='Order Reference', required=True)
    date_order = fields.Datetime(string='Order Date')
    customer_id = fields.Many2one('crm.juno.customer', string='Customer')
    product_ids = fields.Many2many('my_facturacion.producto', string='Products')

    @api.model
    def create_order(self, name, date_order, customer_id, product_ids):
        vals = {
            'name': name,
            'date_order': date_order,
            'customer_id': customer_id,
            'product_ids': [(6, 0, product_ids)] if product_ids else False,
        }
        return self.env['crm.juno.order'].create(vals)

class Producto(models.Model):
    _name = 'my_facturacion.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre del Producto', required=True)
    precio = fields.Float(string='Precio')

    @api.model
    def create(self, vals):
        return super(Producto, self).create(vals)

class potencialcustomer(models.Model):
    _name = 'crm_modulo.potential_customer'
    _description = 'Potential Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    customer_id = fields.Many2one('crm.juno.customer', string='Related Customer')
    description = fields.Text(string='Description')

    @api.model
    def create_potential_customer(self, name, email=None, phone=None, address=None, customer_id=None, description=None):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'customer_id': customer_id,
            'description': description,
        }
        return self.env['crm_modulo.potential_customer'].create(vals)