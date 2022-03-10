from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def root():
    return {'Hello': 'World'}
