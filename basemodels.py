from typing import Optional, List

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

class Header(BaseModel):
    logo: Optional[str] = '/Images/logo.png'
    title: str = 'PhysioCam Program'

class Exercise(BaseModel):
    images: List[str]
    description: str


class Footer(BaseModel):
    contact: str = 'This is the contact info or whatever'


class Program(BaseModel):
    header: Header
    exercises : List[Exercise]
    footer: Footer

class Request(BaseModel):
    recipient_email: str
    confirmation_email: Optional[List[str]]
    program: Program

    