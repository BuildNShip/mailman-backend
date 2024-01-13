from enum import Enum


class MailServerConfKey(Enum):
    HOST = 'host'
    PORT = 'port'


mail_providers_list = {
    'gmail': {MailServerConfKey.HOST.value: 'smtp.gmail.com', MailServerConfKey.PORT.value: 587},
    'yahoo': {MailServerConfKey.HOST.value: 'smtp.mail.yahoo.com', MailServerConfKey.PORT.value: 587},
    'ses': {MailServerConfKey.HOST.value: 'email-smtp.us-east-1.amazonaws.com', MailServerConfKey.PORT.value: 587},
    'zoho': {MailServerConfKey.HOST.value: 'smtp.zoho.com', MailServerConfKey.PORT.value: 587}
}
