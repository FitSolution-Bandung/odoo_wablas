from odoo import models, fields, api, exceptions
import requests
import json
import re


class WhatsappMessage(models.Model):
    _name = 'whatsapp.message'
    _description = 'WhatsApp Message'

    name = fields.Char(string='Name', readonly=True)
    sender = fields.Char(string='Sender', readonly=True )
    recipient = fields.Char(string='Recipient', readonly=True)
    message = fields.Text(string='Message', readonly=True)
    message_type = fields.Selection(
        selection=[('text', 'Text'), ('document', 'Document')],
        string='Message Type',
        default=None,
        readonly=True
    )
      
    attachment_id = fields.Many2one('ir.attachment', string='Attachment', readonly=True)
    status = fields.Selection(
        selection=[('sent', 'Sent'), ('failed', 'Failed')],
        string='Status',
        default=None, readonly=True
    )

    sent_at = fields.Datetime(string='Sent At', readonly=True)



