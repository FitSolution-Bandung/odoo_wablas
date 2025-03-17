from odoo import models, fields, api, exceptions
import requests
from requests.exceptions import RequestException
from .send_via_wablas import SendViaWablas
import re
import json


class WhatsAppComposeMessage(models.TransientModel, SendViaWablas):
    _inherit = 'mail.compose.message'

    quotation_id = fields.Many2one('sale.order', string='Quotation')

    whatsapp_message = fields.Text(
        string='WhatsApp Message', compute='_compute_whatsapp_message')

    @api.depends('body')
    def _compute_whatsapp_message(self):
        for record in self:
            record.whatsapp_message = self.convert_html_to_whatsapp(
                record.body)

    def send_whatsapp(self):
        # quotation = self.quotation_id or self.env['sale.order'].browse(
        #     self.env.context.get('active_id'))
        
        partner_ids = self.partner_ids

        error_msg = ""
        for partner in partner_ids:
            if partner.mobile:
                self.send_via_wablas(partner.mobile, partner.name, self.whatsapp_message, self.attachment_ids)
            else:
                error_msg += "No mobile number is set for the partner: " + partner.name

        if error_msg != "":
            raise exceptions.UserError(error_msg)
