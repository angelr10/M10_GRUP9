from odoo import models, fields, api

class my_ventas(models.Model):
    _name = 'my_ventas.my_ventas'
    _description = 'my_ventas.my_ventas'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class Ventas(models.Model):
    _name = 'my_ventas.ventas'
    _description = 'Ventas'

    name = fields.Char(string='Nombre')
    fecha = fields.Date(string='Fecha')
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    producto_ids = fields.Many2many('my_facturacion.producto', string='Productos')
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    estado = fields.Selection([('borrador', 'Borrador'), ('confirmado', 'Confirmado'), ('entregado', 'Entregado')], 
                              string='Estado', default='borrador')

    @api.depends('producto_ids')
    def _compute_total(self):
        for venta in self:
            total = sum(producto.precio for producto in venta.producto_ids)
            venta.total = total

    def action_confirmar_venta(self):
        self.estado = 'confirmado'

    def action_entregar_venta(self):
        self.estado = 'entregado'

class Cliente(models.Model):
    _name = 'my_ventas.cliente'
    _description = 'Clientes'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')

class Producto(models.Model):
    _name = 'my_facturacion.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre del Producto', required=True)
    precio = fields.Float(string='Precio')

    @api.model
    def create(self, vals):
        return super(Producto, self).create(vals)
