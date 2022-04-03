import re
import requests
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from os import environ

# get SMTP configuration from environment variable
SMTP_HOSTNAME = environ.get('SMTP_HOSTNAME')
SMTP_USE_STARTTLS = (environ.get('SMTP_USE_STARTTLS') == True)
SMTP_PORT = environ.get('SMTP_PORT')
SMTP_USERNAME = environ.get('SMTP_USERNAME')
SMTP_PASSWORD = environ.get('SMTP_PASSWORD')

# validate if required options are present
assert SMTP_HOSTNAME, 'SMTP_HOSTNAME is not configured!'

# set default SMTP port number if not configured
# default = 25 for non-STARTTLS. 587 for STARTTLS
if not SMTP_PORT and SMTP_USE_STARTTLS:
    SMTP_PORT = 587
elif not SMTP_PORT:
    SMTP_PORT = 25

# get hCaptcha secret key from environment variable
HCAPTCHA_SECRET = environ.get('HCAPTCHA_SECRET')


def send_mail(mail_from, mail_to, subject, body, reply_to=None):
    '''
    Send a plaintext email.
    Paramenters: from address, to address, subject, email body/content,
                 reply-to address (optional)
    '''
    with smtplib.SMTP(SMTP_HOSTNAME, SMTP_PORT) as server:
        # STARTTLS
        if SMTP_USE_STARTTLS:
            server.ehlo()
            server.starttls()
            server.ehlo()
        # authenticate with SMTP server
        if SMTP_USERNAME and SMTP_PASSWORD:
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
