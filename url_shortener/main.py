# by Richi Rod AKA @richionline / falken20
# url_shortener/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the URL Shortener API"