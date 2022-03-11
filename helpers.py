import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from os import environ

# getSMTP configuration from environment variable
smtp_config = {
    'hostname': environ.get('SMTP_HOSTNAME'),
    'port': environ.get('SMTP_SSL_PORT'),
    'username': environ.get('SMTP_USERNAME'),
    'password': environ.get('SMTP_PASSWORD'),
}

# validate if required options are present
assert smtp_config['hostname'], 'SMTP_HOSTNAME is not configured!'
assert smtp_config['port'], 'SMTP_SSL_PORT is not configured!'

# create a secure SSL context
ssl_context = ssl.create_default_context()


def send_mail(mail_from, mail_to, subject, body, reply_to=None):
    with smtplib.SMTP_SSL(smtp_config['hostname'], smtp_config['port'],
                          context=ssl_context) as server:
        # authenticate with SMTP server
        server.login(smtp_config['username'], smtp_config['password'])
        # build mail message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg.set_content(body)
        # set Reply-To if provided
        if reply_to:
            msg['Reply-To'] = reply_to
        # send plain text mail with subject
        server.send_message(msg)
