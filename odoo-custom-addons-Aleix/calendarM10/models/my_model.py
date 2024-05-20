# models/my_model.py

from odoo import models, fields

class CalendarEvent(models.Model):
    _name = 'calendar.event'
    _description = 'Evento de Calendario'

    name = fields.Char(string="Título", required=True)
    start_datetime = fields.Datetime(string="Hora de Inicio", required=True)
    end_datetime = fields.Datetime(string="Hora de Fin", required=True)
    event_type = fields.Selection([
        ('marketing', 'Marketing'),
        ('launch', 'Lanzamiento de Producto'),
        ('other', 'Otro')
    ], string="Tipo de Evento", default='other')
    impact_expected = fields.Text(string="Impacto Esperado")
    description = fields.Text(string="Descripción")
    location = fields.Char(string="Ubicación")
    all_day = fields.Boolean(string="Evento Todo el Día")
