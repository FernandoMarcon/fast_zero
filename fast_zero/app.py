from fastapi import FastAPI
from http import HTTPStatus
from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message


app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_test():
    return """
    <html>
        <head>
        <title> Olá Mundo! </title>
        </head>
        <body>
            <h1>Olá Mundo! </h1>
        </body>
    </html>
    """
