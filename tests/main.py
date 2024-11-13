#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# cython: language_level=3
from pathlib import Path

from fastapi import FastAPI, HTTPException

from fastapi_app_ext import AppExt

root_path = Path(__file__).absolute().parent.parent

app = FastAPI()
AppExt(app, root_path)


@app.get('/')
async def index():
    raise HTTPException(status_code=404,detail='Not Found')
