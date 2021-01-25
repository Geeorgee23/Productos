# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class clientes_model(models.Model):
    _name = 'productos_app.clientes_model'
    _description = 'productos_app.clientes_model'

    name = fields.Char(string="Nombre", size=20, required=True)
    dni= fields.Char(string="DNI", size=9, required=True, index=True)
    foto = fields.Binary()
    apellidos = fields.Char(string="Apellidos", size=50)
    telf = fields.Char(string="Telefono", size=9)
    email = fields.Char(string="Email", size=50)

    factura = fields.One2many("productos_app.facturas_model","cliente", string="Facturas")



    @api.constrains("dni")
    def _validarDni(self):
        letras="TRWAGMYFDPXBNJZSQVHLCKE"

        letra =self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError ("DNI Invalido!")


    @api.constrains("email")
    def is_valid_email(self):
        if "@" and "." not in self.email:
            raise ValidationError("Email Invalido!")



    