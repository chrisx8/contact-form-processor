from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import environ
from router import router

# start FastAPI app
description = '''
### A fast and simple contact form processor/handler, powered by FastAPI.\n
Submit a contact form in JSON via POST requests to `/contact/`, and if the form
is valid, an email will be sent to the site owner.
'''
app = FastAPI(
    title='contact-form-processor',
    version='0.1.0',
    description=description,
    license_info={
        "name": "GNU AGPLv3",
        "url": "https://www.gnu.org/licenses/agpl-3.0.en.html",
    },
)

# fun CORS stuff
try:
    # try to configure CORS origins from `CORS_ALLOWED_ORIGINS`
    CORS_ORIGINS = environ['CORS_ALLOWED_ORIGINS'].split(',')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_methods=['POST', 'HEAD', 'OPTIONS'],
    )
except KeyError:
    # not configured, no CORS
    pass

# load main router
app.include_router(router)
