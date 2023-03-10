from django.urls import path

from .views import SendMail,SendBulkMail

urlpatterns = [
    path('send-bulk-mail', SendBulkMail.as_view(), name="send_bulk_mail"),
    path('send-mail', SendMail.as_view(), name="send_mail"),
]