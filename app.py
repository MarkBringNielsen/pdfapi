from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from basemodels import Request
from generator import data_to_html
from mailing_service import send_email

app = FastAPI()


@app.get('/')
async def read_root():
    return {'Hello' : 'World'}

@app.post('/api/programs/')
async def update_program(request: Request):

    file_id = data_to_html(request.program)
    send_email(file_id, None)
    return 
