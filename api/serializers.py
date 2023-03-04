from django.core.validators import EmailValidator
from rest_framework import serializers


class MailValidateSerializer(serializers.Serializer):
    fromMail = serializers.EmailField(validators=[EmailValidator(message='Invalid email address.')])
    inputFile = serializers.FileField()
    mailAttachment = serializers.FileField(required=False)
    content = serializers.CharField()
    subject = serializers.CharField()

    # def validate_file(self, file):
    #     if file.size > 1024 * 1024:
    #         raise serializers.ValidationError('File size must be less than 1 MB.')
    #     return file

    def validate_content(self, content):
        if len(content) < 10:
            raise serializers.ValidationError('Content must be at least 10 characters.')
        return content

    def validate_subject(self, subject):
        if len(subject) < 5:
            raise serializers.ValidationError('Subject must be at least 5 characters.')
        return subject
