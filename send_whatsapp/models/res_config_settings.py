from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wablas_token = fields.Char(string='Wablas Token', config_parameter='wablas_token')
    wablas_api_url = fields.Char(string='Wablas API URL', config_parameter='wablas_api_url')

    wablas_qr_code_link = fields.Char(string='Wablas QR Code Link', compute= '_compute_wablas_qr_code_link', widget="url")

    @api.depends('wablas_api_url', 'wablas_token')
    def _compute_wablas_qr_code_link(self):
        for record in self:
            if record.wablas_api_url and record.wablas_token:
                record.wablas_qr_code_link = f"{record.wablas_api_url}/api/device/scan?token={record.wablas_token}"
            else:
                record.wablas_qr_code_link = ''

    def action_open_wablas_qr_code(self):
        return {
            'type': 'ir.actions.act_url',
            'url': self.wablas_qr_code_link,
            'target': 'new',
        }
    

    # def action_open_wablas_qr_code(self):
    #     self.ensure_one()
    #     view = self.env.ref('send_whatsapp.view_wablas_qrcode_wizard_form')
    #     wizard = self.env['wablas.qrcode.wizard'].create({'qr_code_link': self.wablas_qr_code_link})
        
    #     return {
    #         'name': 'Wablas QR Code',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'wablas.qrcode.wizard',
    #         'views': [(view.id, 'form')],
    #         'view_id': view.id,
    #         'target': 'new',
    #         'res_id': wizard.id,
    #         'context': self.env.context,
    #     }




class WablasQRCodeWizard(models.TransientModel):
    _name = 'wablas.qrcode.wizard'
    _description = 'Wablas QR Code Wizard'

    qr_code_link = fields.Char(string='QR Code Link', readonly=True)