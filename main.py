from fastapi import FastAPI, Form, Response, status
from os import environ
from helpers import send_mail, verify_hcaptcha
from models import Message

# get config options from environment variable
MAIL_FROM = environ.get('MAIL_FROM')
MAIL_TO = environ.get('MAIL_TO')

# start FastAPI app
app = FastAPI()


@app.get('/')
async def root():
    '''
    The root route.\n
    Does nothing, other than returning 'Hello world!' in JSON.
    '''
    return {'message': 'Hello world!'}


@app.post('/contact/form/')
async def submit_contact_form(response: Response,
                              name: str = Form(...),
                              email: str = Form(...),
                              subject: str = Form(...),
                              message: str = Form(...),
                              h_captcha_response: str = Form(...)):
    '''
    Processes contact form submission.\n
    Accepts an HTML form via a POST request and validates form data and the
    hCaptcha.\n
    If validation passes, send email to site owner, and return success message 
    in JSON. Otherwise, return an error message in JSON.
    '''
    # TODO: validate email address

    # verify hCaptcha response
    if not verify_hcaptcha(hcaptcha_response):
        # error if verification fails
        response.status_code = 400
        return {'error': 'CAPTCHA verification failed. Please try again.'}

    # inject into message for outgoing mail
    subject = '[CONTACT FORM]' + subject
    message += '\n\n' + '-' * 80 + f'\nMessage from {name} - {email}'

    send_mail(MAIL_FROM, MAIL_TO, subject, message, reply_to=email)
    return {'message': 'success'}
