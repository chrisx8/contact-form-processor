from fastapi import APIRouter, Response, status
from os import environ
from helpers import send_mail, validate_email, verify_hcaptcha
from models import Message

# get config options from environment variable
MAIL_FROM = environ.get('MAIL_FROM')
MAIL_TO = environ.get('MAIL_TO')

# check if MAIL_FROM and MAIL_TO is configured
assert MAIL_FROM, 'MAIL_FROM is not configured!'
assert MAIL_TO, 'MAIL_TO is not configured!'

# create API router
router = APIRouter()


@router.get('/')
async def root():
    '''
    The root route.\n
    Does nothing, other than returning 'Hello world!' in JSON.
    '''
    return {'message': 'Hello world!'}


@router.post('/contact/')
async def submit_contact_form(msg: Message, resp: Response):
    '''
    Processes contact form submission.\n
    Accepts JSON via a POST request and validates form data and the hCaptcha
    response.\n
    If validation passes, send email to site owner, and return success message 
    in JSON. Otherwise, return an error message in JSON.
    '''
    # validate email address
    if not validate_email(msg.email):
        # error if verification fails
        resp.status_code = 400
        return {'message': 'Please enter a valid email address.'}

    # verify hCaptcha response
    if not verify_hcaptcha(msg.h_captcha_response):
        # error if verification fails
        resp.status_code = 400
        return {'message': 'CAPTCHA verification failed. Please try again.'}

    # inject into message for outgoing mail
    from_name = f'{msg.name} <{MAIL_FROM}>'
    reply_to_name = f'{msg.name} <{msg.email}>'
    subject = f'[CONTACT FORM] {msg.subject}'
    body = f'{msg.message}\n\n' + '-' * 80 + '\n' + \
        f'Message from {msg.name} - {msg.email}'

    send_mail(from_name, MAIL_TO, subject, body, reply_to=reply_to_name)
    return {'message': 'Your message has been sent successfully. Thanks for reaching out!'}
