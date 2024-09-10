# FastAPI AppExt

---

**Source Code**: <a href="https://github.com/hgz1989/fastapi-app-ext" target="_blank">https://github.com/hgz1989/fastapi-app-ext</a>

---

Installation
------------

``pip install fastapi-app-ext``


Hello World Example
-------------------

.. code:: python

    from fastapi import FastAPI
    from fastapi-app-ext import AppExt

    app = FastAPI(title='Hollo World Example')
    AppExt(app)

    @app.get('/')
    async def index():
        return {'hello': 'world'}

    if __name__ == '__main__':
        import uvicorn
        uvicorn.run(app)