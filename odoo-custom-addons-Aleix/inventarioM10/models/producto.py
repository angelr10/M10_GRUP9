from odoo import models, fields

class Producto(models.Model):
    _name = 'x_inventarioM10_producto'
    _description = 'Producto'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    cantidad = fields.Integer(string="Cantidad en Stock")
