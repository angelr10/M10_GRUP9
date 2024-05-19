# -*- coding: utf-8 -*-

# models/models.py
from odoo import models, fields

class M10testu01(models.Model):
    _name = 'm10testu01'
    _description = 'Descripción de M10testu01'

    name = fields.Char(string='Nombre')

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#
# class moto(models.Model):
#	_modelo = 'moto.moto'
#	_años = 'moto.moto'
#	
#	modelo = fields.Char()
#	años = fields.Integer()
