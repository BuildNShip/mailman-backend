import json
from typing import Dict

import requests
from decouple import config
from django.core.mail import get_connection

from utils.mail_providers import mail_providers_list
from utils.date_util import DateUtil


class EmailUtil:
    @staticmethod
    def make_connection(request_data: Dict):
        """
        Create an email connection based on the provided request_data.

        :param request_data: A dictionary containing email-related configuration data.
            It should include keys such as 'mail_server', 'from_mail', and 'password'.
        :return: An email connection object.
        """
        # Retrieve email configuration from Django settings or environment variables
        host, port = config('EMAIL_HOST'), config('EMAIL_PORT')

        mail_server = request_data.get('mail_server')
        if mail_server:
            # If a specific mail server is specified in the request data,
            # override the default settings with the values from the mail_providers dictionary
            host, port = mail_providers_list.get(mail_server)

        # Extract email credentials from the request_data
        EMAIL_HOST_USER = request_data.get('from_mail')
        EMAIL_HOST_PASSWORD = request_data.get('password')

        # Configure the email connection with TLS enabled
        EMAIL_USE_TLS = True

        # Create and return the email connection
        connection = get_connection(
            host=host, port=port, username=EMAIL_HOST_USER,
            password=EMAIL_HOST_PASSWORD, use_tls=EMAIL_USE_TLS
        )
        return connection


class LogUtils:
    @staticmethod
    def logs_dumper(request, email_address, status):
        """
        Dump logs related to email activities to a specified TEXTDB_URL.

        :param request: The HTTP request object.
        :param email_address: The email address associated with the logs.
        :param status: A boolean indicating the success or failure of the email activity.
        :return: The response object from the HTTP request to TEXTDB_URL.
        """
        # Get the TEXTDB_URL from the configuration
        URL = config("TEXTDB_URL")

        # Make a GET request to retrieve existing logs from TEXTDB_URL
        response = requests.get(URL)

        # Initialize or load existing logs from the response text
        if response.text == '':
            JSON_LOGS = {
                "number_of_mails": 0,
                "successful_mails": 0,
                "unsuccessful_mails": 0,
                "entries": []
            }
        else:
            JSON_LOGS = json.loads(response.text)

        # Prepare the logs for the current email activity
        query_logs = {
            'from_mail': email_address,
            'datetime': str(DateUtil.get_current_utc_time()),
            "location": request.headers.get('location', 'Unknown'),
            'ip_address': request.headers.get('x-real-ip', 'Unknown'),
            'userAgent': request.headers.get("User-Agent", 'Unknown')
        }

        # Update the number of successful and unsuccessful mails in the logs
        if status:
            JSON_LOGS["successful_mails"] += 1
        else:
            JSON_LOGS["unsuccessful_mails"] += 1

        # Append the current query_logs to the entries in the logs
        JSON_LOGS["entries"].append(query_logs)

        # Update the total number of mails in the logs
        JSON_LOGS["number_of_mails"] = JSON_LOGS["successful_mails"] + JSON_LOGS["unsuccessful_mails"]

        # Make a POST request to update the logs at TEXTDB_URL
        requests.post(URL, json=JSON_LOGS)

        # Return the response from the initial GET request
        return response
