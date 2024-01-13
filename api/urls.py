from django.urls import path

from .views import SendMail, ListMailProvidersView

urlpatterns = [
    path('send-mail/', SendMail.as_view(), name="send_mail"),
    path('list-mail-providers/', ListMailProvidersView.as_view(), name="list_mail_providers")
]
