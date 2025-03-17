from odoo import models, fields, api, exceptions
import requests
import json
import re


class SendViaWablas(models.AbstractModel):
    _name = 'send.via.whatsapp'
    _description = 'Send WhatsApp Message via Wablas'

    def send_via_wablas(self, mobile_number, partner_name, message, attachment_ids=None):
        token = self.env['ir.config_parameter'].sudo(
        ).get_param('wablas_token')
        url = self.env['ir.config_parameter'].sudo(
        ).get_param('wablas_api_url')

        if not token or not url:
            raise exceptions.UserError(
                "Wablas token or URL is not set in system configuration")

        headers = {'Authorization': token}

        # definiikan end point untuk mengirim dokumen
        if url.endswith('/'):
            url = url[:-1]

        if attachment_ids:
            endpoint = url + '/api/send-document-from-local'
            message_type = 'document'

        data = {
            'phone': mobile_number,
        }

        if attachment_ids == None:
            endpoint = url + '/api/send-message'
            message_type = 'text'

            data.update({
                'message': message,
            })

            try:
                response = requests.post(
                    endpoint, headers=headers, data=data)
                if response.status_code == 200:
                    status = 'sent'
                    print("response.json(): ", response.json())
                else:
                    status = 'failed'
                    print("response.json(): ", response.json())

            except Exception as e:
                status = 'failed'
                print("Error: ", e)

            self.add_whatsapp_history(
                self, partner_name, mobile_number, message, message_type, status, None)

        else:
            endpoint = url + '/api/send-document-from-local'
            message_type = 'document'

            i = 0
            for attachment in reversed(attachment_ids):
                i += 1
                file_content = attachment.datas
                file_name = attachment.name
              
                if i == 1:
                    caption = message
                else:
                    caption = file_name
                    message = caption

                data.update({
                    'caption': caption,
                    'file': file_content,
                    'name_file': file_name,
                    'data': json.dumps({
                            'name': file_name,
                            })
                })

                try:
                    response = requests.post(
                        endpoint, headers=headers, data=data)
                    if response.status_code == 200:
                        status = 'sent'
                        print("response.json(): ", response.json())
                    else:
                        status = 'failed'
                        print("response.json(): ", response.json())
                        
                except Exception as e:
                    status = 'failed'
                    print("Error: ", e)

                self.add_whatsapp_history(
                    self, partner_name, mobile_number, message, message_type, status, attachment)
                




    @staticmethod
    def add_whatsapp_history(self, partner_name, mobile_number,  message, message_type, status, attachment_id = None):

        attachment_ref = attachment_id.id if attachment_id else False

        self.env['whatsapp.message'].create({
            'name': partner_name,
            'sender': self.env.user.name,
            'recipient': mobile_number,
            'message': message,
            'message_type': message_type,
            'sent_at': fields.Datetime.now(),
            'status': status,
            'attachment_id': attachment_ref

        })

    @staticmethod
    def convert_html_to_whatsapp(html_content):

        html_content = html_content.replace('\n', '')

        # Mengganti teks tebal
        html_content = re.sub(r'<b>(.*?)</b>', r'*\1*', html_content)
        html_content = re.sub(r'<strong>(.*?)</strong>', r'*\1*', html_content)
        html_content = re.sub(
            r'<span style="font-weight:bold;">(.*?)</span>', r'*\1*', html_content)

        # Mengganti teks miring
        html_content = re.sub(r'<i>(.*?)</i>', r'_\1_', html_content)
        html_content = re.sub(r'<em>(.*?)</em>', r'_\1_', html_content)

        # Mengganti baris baru
        html_content = re.sub(r'\s+', ' ', html_content)
        html_content = re.sub(r'<br\s*(.*?)>', '\n', html_content)
        html_content = re.sub(r'\n\n\s+', '\n\n', html_content)

        # Further cleaning if necessary
        html_content = html_content.strip()  # Remove leading/trailing whitespace

        # Menghapus semua tag HTML lainnya
        html_content = re.sub(r'<[^>]+>', '', html_content)

        return html_content
