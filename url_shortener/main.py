# by Richi Rod AKA @richionline / falken20
# url_shortener/main.py

# FastAPI creates documentation of your API endpoints for you.
# Go check it out in your browser at:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI, HTTPException
import validators  # To validate URLs, email addresses, IP addresses, etc.

from . import schemas

app = FastAPI()


@app.get("/")
@app.get("/home")
def main():
    return "Welcome to the URL Shortener API \nThese are the endpoints:"


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    
    return f"TODO: Create database entry for: {url.target_url}"