from odoo import models, fields, api, exceptions
import requests
import re
from odoo.modules.module import get_module_resource
import os
import base64
import json
from .send_via_wablas import SendViaWablas



class AccountInvoiceSend(models.TransientModel, SendViaWablas):
    _inherit = 'account.invoice.send'

    whatsapp_message = fields.Text(
        string='WhatsApp Message', compute='_compute_whatsapp_message')

    @api.depends('body')
    def _compute_whatsapp_message(self):
        for record in self:
            record.whatsapp_message = self.convert_html_to_whatsapp(record.body)
 

        # return res

    def send_whatsapp(self):
        # self.ensure_one()
        invoice_id = self.env.context.get('active_id')
        if not invoice_id:
            raise exceptions.UserError("No active invoice found.")

        # Dapatkan objek invoice
        invoice = self.env['account.move'].browse(invoice_id)
        if not invoice:
            raise exceptions.UserError("Invoice not found.")

        partner_ids = self.partner_ids

        # Kirim pesan ke semua partner
        error_msg = ""
        for partner in partner_ids:
            if partner.mobile:
                # self.send_invoice_pdf_whatsapp(partner.mobile, partner.name, self.whatsapp_message)
                self.send_via_wablas(partner.mobile, partner.name, self.whatsapp_message, self.attachment_ids)
            
            
            else:
                error_msg += "No mobile number is set for the partner: " + partner.name
                    

        if error_msg != "":
            raise exceptions.UserError(error_msg)
    
