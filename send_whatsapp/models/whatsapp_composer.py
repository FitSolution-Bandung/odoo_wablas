import requests
from odoo import models, fields, api, exceptions
from requests.exceptions import RequestException
from .send_via_wablas import SendViaWablas


class WhatsappComposer(models.TransientModel, SendViaWablas):
    _name = 'whatsapp.composer'
    _description = 'WhatsApp Message Composer'

    partner_id = fields.Many2one(
        'res.partner', string="Recipient", required=True)
    mobile = fields.Char(related='partner_id.mobile',
                         string="Mobile Number", readonly=True)
    message = fields.Text(string="Message", required=True)



    def default_get(self, fields):
        res = super(WhatsappComposer, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if 'partner_id' in fields and active_id:
            res.update({'partner_id': active_id})
        return res

    def action_send_message(self):
        # Ambil data dari record ini
        mobile_number = self.mobile
        message = self.message
        partner_name = self.partner_id.name


        if not mobile_number:
            raise exceptions.UserError(
                "No mobile number is set for the partner: " + self.partner_id.name)
        

        # Kirim pesan menggunakan Wablas
        # self._send_message_via_wablas(mobile_number, partner_name, message)
        self.send_via_wablas(mobile_number, partner_name, message)


       
        