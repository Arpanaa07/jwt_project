# utils.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.core.mail import send_mail
from django.conf import settings

def send_reset_email(email, reset_link):
    subject = 'Password Reset Request'
    message = f'Click the link below to reset your password:\n{reset_link}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()
