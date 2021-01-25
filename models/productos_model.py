# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos_model(models.Model):
    _name = 'productos_app.productos_model'
    _description = 'productos_app.productos_model'

    name = fields.Char(string="Referencia",help="Nombre del producto", size=20, required=True)
    descripcion = fields.Html(string="Descripcion",help="Descripcion del producto")
    pvp = fields.Float(string="Precio",help="Precio del producto")