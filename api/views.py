from smtplib import SMTPRecipientsRefused, SMTPAuthenticationError

from django.core import mail
from rest_framework.views import APIView

from utils.mail_providers import mail_providers_list
from utils.response import CustomResponse
from utils.utils import EmailUtil, LogUtils


class SendMail(APIView):
    def post(self, request):
        """
        Handles the HTTP POST request to send an email.

        :param request: The HTTP request object.
        :return: HTTP response indicating the status of the email sending process.
        """
        # Extract necessary information from the request data
        request_data = request.data
        subject = request_data.get('subject')
        content = request_data.get('content')
        from_mail = request_data.get('from_mail')
        to_mail = request_data.get('to')
        message_type = request_data.get('message_type', 'text')

        # Get attachments from the request
        mail_attachments = request.FILES.getlist('mail_attachment')

        # Create an email connection using EmailUtil
        connection = EmailUtil.make_connection(request_data)

        # Create an EmailMessage object with the specified details
        email = mail.EmailMessage(
            subject=subject,
            body=content,
            from_email=from_mail,
            to=[to_mail],
            connection=connection,
        )

        # Set content_subtype to 'html' if message_type is 'html'
        if message_type.lower() == 'html':
            email.content_subtype = 'html'

        # Attach files to the email
        for mail_attachment in mail_attachments:
            email.attach(mail_attachment.name, mail_attachment.read(), mail_attachment.content_type)

        try:
            # Attempt to send the email
            status = email.send()

            # Close the email connection
            connection.close()

            # Log the email sending status
            LogUtils.logs_dumper(request, from_mail, status)

            # Return a success response
            return CustomResponse(general_message="Mail successfully sent",
                                  response={"recipient": to_mail}).get_success_response()

        except SMTPRecipientsRefused:
            # Handle invalid recipient address
            status = 0
            LogUtils.logs_dumper(request, from_mail, status)
            return CustomResponse(general_message="Invalid mail address",
                                  response={"recipient": to_mail}).get_failure_response(status_code=1001)

        except ValueError:
            # Handle invalid recipient address
            status = 0
            LogUtils.logs_dumper(request, from_mail, status)
            return CustomResponse(general_message="Invalid mail address",
                                  response={"recipient": to_mail}).get_failure_response(status_code=1001)

        except SMTPAuthenticationError:
            # Handle invalid 'from' mail or password
            status = 0
            LogUtils.logs_dumper(request, from_mail, status)
            return CustomResponse(general_message="Invalid from mail or password",
                                  response={"recipient": to_mail}).get_failure_response(status_code=1001)


class ListMailProvidersView(APIView):
    def get(self, request):
        """
        Handles the HTTP GET request to retrieve a list of mail providers.

        :param request: The HTTP request object.
        :return: HTTP response containing the list of mail providers.
        """

        # Return a success response with the list of mail providers
        return CustomResponse(response=mail_providers_list.keys()).get_success_response()
