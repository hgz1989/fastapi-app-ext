#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# cython: language_level=3
from fastapi import FastAPI

from fastapi_app_ext import AppExt

app = FastAPI()
AppExt(app)


@app.get('/')
async def index():
    return {'hello': 'world'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
