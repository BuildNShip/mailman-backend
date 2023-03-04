from django.urls import path

from .views import SendBulkMail

urlpatterns = [
    path('send-mail', SendBulkMail.as_view(), name="send_bulk_mail"),
]