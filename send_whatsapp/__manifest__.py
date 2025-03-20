# -*- coding: utf-8 -*-
{
    'name': "MESSAGO - Send Quotation/Invoices to Whatsapp",
    'summary': "Addon ini mengizinkan pengguna untuk mengirim lampiran langsung melalui layanan pesan WhatsApp.",
    'description': """
        Addon ini mengizinkan pengguna untuk mengirim 
        lampiran langsung melalui layanan pesan WhatsApp memungkinkan 
        pengguna Odoo untuk dengan mudah mengirim berupa dokumen ke kontak 
        WhatsApp tertentu dari dalam platform Odoo.

    """,
    'application': True,
    'images': ['static/description/icon.png'],
    'author': "PT. Fujicon Priangan Perdana",
    'website': "https://www.fujicon-japan.com",
    'category': 'Extra Tools',
    'version': '0.1.1',
    'sequence': -100,
    'images': ['images/wablas.gif'],
    'depends': ['base', 'account','sale_management','contacts'],
    'license': 'OPL-1',
    'data': [
        'security/ir.model.access.csv',
        'views/mail_compose_message_views.xml',
        'views/whatsapp_message_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/whatsapp_composer_views.xml', 
        'views/account_invoice_send_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
