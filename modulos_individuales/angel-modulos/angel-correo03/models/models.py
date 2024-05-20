from odoo import models, fields

class Emails01(models.Model):
    _name = 'emails_01'
    _description = 'Emails 01'

    campo_texto1 = fields.Char(string="Campo de Texto 1", required=True)
    campo_texto2 = fields.Char(string="Campo de Texto 2", required=True)
    def guardar(self):
        return True