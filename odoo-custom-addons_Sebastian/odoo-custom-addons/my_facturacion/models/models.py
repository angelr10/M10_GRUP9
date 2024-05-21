from odoo import models, fields, api

class my_facturacion(models.Model):
    _name = 'my_facturacion.my_facturacion'
    _description = 'my_facturacion.my_facturacion'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class factura(models.Model):
    _name = 'my_facturacion.factura'
    _description = 'Factura'

    name = fields.Char(string='Número de Factura', required=True)
    fecha = fields.Date(string='Fecha de Factura')
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    total = fields.Float(string='Total')

    @api.model
    def create(self, vals):
        return super(factura, self).create(vals)


class lineaFactura(models.Model):
    _name = 'my_facturacion.linea_factura'
    _description = 'Línea de Factura'

    factura_id = fields.Many2one('my_facturacion.factura', string='Factura')
    producto_id = fields.Many2one('product.product', string='Producto')
    cantidad = fields.Float(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for linea in self:
            linea.subtotal = linea.cantidad * linea.precio_unitario

    @api.model
    def create(self, vals):
        return super(lineaFactura, self).create(vals)


class Producto(models.Model):
    _name = 'my_facturacion.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre del Producto', required=True)
    precio = fields.Float(string='Precio')

    
