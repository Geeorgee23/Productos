# -*- coding: utf-8 -*-
# from odoo import http


# class ProductosApp(http.Controller):
#     @http.route('/productos_app/productos_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/productos_app/productos_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('productos_app.listing', {
#             'root': '/productos_app/productos_app',
#             'objects': http.request.env['productos_app.productos_app'].search([]),
#         })

#     @http.route('/productos_app/productos_app/objects/<model("productos_app.productos_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('productos_app.object', {
#             'object': obj
#         })
