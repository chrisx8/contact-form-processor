from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    name: str
    email: str
    subject: str
    message: str
    hcaptcha_response: str
