from odoo import models, fields

class Empleado(models.Model):
    _name = 'empleadosm10.empleado'
    _description = 'Gestión de Empleados'

    nombre = fields.Char(string="Nombre Completo", required=True)
    identificacion = fields.Char(string="Identificación", required=True)
    puesto = fields.Char(string="Puesto de Trabajo")
    departamento = fields.Char(string="Departamento")
    email = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")
    imagen = fields.Image(string="Foto")

