from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>Hello Labs!</title>
        </head>
        <body>
            <h1>Hello from app №1</h1>
            <a href="https://www.youtube.com/watch?v=HIcSWuKMwOw">Всем привет</a>
        </body>
    </html>
    """
    return html_content
