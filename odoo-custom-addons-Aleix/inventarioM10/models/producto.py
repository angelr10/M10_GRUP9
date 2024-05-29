from odoo import models, fields

class Producto(models.Model):
    _name = 'inventariom10.producto'
    _description = 'Producto de Ropa para Niños'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    cantidad = fields.Integer(string="Cantidad en Stock")
    tipo_producto = fields.Selection([
        ('ropa', 'Ropa'),
        ('accesorio', 'Accesorio'),
        ('calzado', 'Calzado')
    ], string="Tipo de Producto", default='ropa')
    precio_venta = fields.Float(string="Precio de Venta")
    coste = fields.Float(string="Coste")
    categoria_producto = fields.Many2one('product.category', string="Categoría de Producto", ondelete='set null')
    imagen = fields.Binary(string="Imagen del Producto")
    material = fields.Char(string="Material")
    talla = fields.Char(string="Talla")
