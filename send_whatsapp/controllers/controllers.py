# -*- coding: utf-8 -*-
from odoo import http
from odoo.modules.module import get_module_resource
import werkzeug
import os



# class SendWhatsapp(http.Controller):
#     @http.route('/send_whatsapp/send_whatsapp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/send_whatsapp/send_whatsapp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('send_whatsapp.listing', {
#             'root': '/send_whatsapp/send_whatsapp',
#             'objects': http.request.env['send_whatsapp.send_whatsapp'].search([]),
#         })

#     @http.route('/send_whatsapp/send_whatsapp/objects/<model("send_whatsapp.send_whatsapp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('send_whatsapp.object', {
#             'object': obj
#         })


