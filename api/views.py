import io

from decouple import config
from django.core import mail
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import get_connection

from .serializers import MailValidateSerializer


class SendBulkMail(APIView):
    def make_connection(self, request_data: dict):
        EMAIL_HOST = config('EMAIL_HOST')
        EMAIL_PORT = config('EMAIL_PORT')
        EMAIL_HOST_USER = request_data.get('fromMail')
        EMAIL_HOST_PASSWORD = request_data.get('password')
        EMAIL_USE_TLS = config('EMAIL_USE_TLS')

        connection = get_connection(host=EMAIL_HOST, port=EMAIL_PORT, username=EMAIL_HOST_USER,
                                    password=EMAIL_HOST_PASSWORD, use_tls=EMAIL_USE_TLS)
        return connection

    def data_from_csv(self, file):
        import csv
        processed_contents = {'headers': [], "dynamic_contents": []}
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        processed_contents['headers'] = next(reader)  # skip header row if present
        for row in reader:
            processed_contents['dynamic_contents'].append(row)
        return processed_contents

    def post(self, request):
        request_data = request.data
        serializer = MailValidateSerializer(data=request_data)
        if not serializer.is_valid():
            return Response({"hasError": True, "message": "Validation Error", "errors": serializer.errors})
        data = self.data_from_csv(request.FILES.get('inputFile'))
        if len(data.get('dynamic_contents'))>50:
            return Response({"hasError": True, "message": "Validation Error", "errors":{
        "inputFile": [
            "To mail should not be more than 50."
        ]
        } })
        mail_attachments = request.FILES.getlist('mailAttachment')
        connection = self.make_connection(request_data)
        # Manually open the connection
        connection.open()
        # Construct an email message that uses the connection
        entries = data.get('dynamic_contents')
        data.get('headers').pop(0)
        headers = data.get('headers')
        content = request_data.get('content')
        for entry_list in entries:
            to_mail = entry_list.pop(0)
            for header in headers:
                new_content = ''
                for entry in entry_list:
                    tag = f'(({header}))'
                    new_content = content.replace(tag, entry)
            email = mail.EmailMessage(
                request_data.get('subject'),
                new_content,
                request_data.get('fromMail'),
                [to_mail],
                connection=connection,
            )
            for mail_attachment in mail_attachments:
                email.attach(mail_attachment.name, mail_attachment.read(), mail_attachment.content_type)
            email.send()  # Send the email
        # We need to manually close the connection.
        connection.close()
        data = {"hasError": False, "message": "success"}
        return Response(data)
