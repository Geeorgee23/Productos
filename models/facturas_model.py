# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class facturas_model(models.Model):
    _name = 'productos_app.facturas_model'
    _description = 'productos_app.facturas_model'

    ref = fields.Char(string="Ref", size=20, required=True)
    fecha = fields.Date(string="Fecha", help="Añade la fecha y la hora", default=datetime.today())
    base = fields.Float(string="Base")
    iva = fields.Selection(string="IVA", selection=[('21','21%'),('2', '15%'),('7', '7%'),('0', '0%')], default='21')
    total = fields.Float(string="Total", compute="_calcularTotal", store=True)

    cliente = fields.Many2one("productos_app.clientes_model", string="Cliente")


    @api.depends('iva', 'base')
    def _calcularTotal(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)

    