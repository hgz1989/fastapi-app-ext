#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# cython: language_level=3
from fastapi import FastAPI

from fastapi_app_ext import AppExt

app = FastAPI()
AppExt(app)


@app.get('/')
async def hello_world():
    return 'Hello World!'
