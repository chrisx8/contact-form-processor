import re
import requests
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from os import environ

# get SMTP configuration from environment variable
SMTP_HOSTNAME = environ.get('SMTP_HOSTNAME')
SMTP_SSL_PORT = environ.get('SMTP_SSL_PORT')
SMTP_USERNAME = environ.get('SMTP_USERNAME')
SMTP_PASSWORD = environ.get('SMTP_PASSWORD')

# validate if required options are present
assert SMTP_HOSTNAME, 'SMTP_HOSTNAME is not configured!'

# set default SMTP port number (465) if not configured
if not SMTP_SSL_PORT:
    SMTP_SSL_PORT = 465

# get hCaptcha secret key from environment variable
HCAPTCHA_SECRET = environ.get('HCAPTCHA_SECRET')

# create a secure SSL context
ssl_context = ssl.create_default_context()


def send_mail(mail_from, mail_to, subject, body, reply_to=None):
    '''
    Send a plaintext email.
    Paramenters: from address, to address, subject, email body/content,
                 reply-to address (optional)
    '''
    with smtplib.SMTP_SSL(SMTP_HOSTNAME, SMTP_SSL_PORT, context=ssl_context) as server:
        # authenticate with SMTP server
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
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


def validate_email(email):
    '''
    Validates an email address.
    Uses an "email address regex that 99.9% works," according to emailregex.com
    Parameter: email address (like 'mail@example.com')
    Returns: True if validation passes. False otherwise.
    '''
    email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    return re.fullmatch(email_regex, email)


def verify_hcaptcha(response):
    '''
    Verify an hCaptcha response token with the hCaptcha API.
    Parameter: hCaptcha response
    Returns: True if verification passes or if hCaptcha credentials are not
             configured, False otherwise
    '''
    # pass check if not configured
    if not HCAPTCHA_SECRET:
        return True
    # validate captcha with API
    req = requests.post('https://hcaptcha.com/siteverify',
                        data={'secret': HCAPTCHA_SECRET, 'response': response})
    # check for success
    return req.json()['success']
