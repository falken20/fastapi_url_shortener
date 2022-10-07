# by Richi Rod AKA @richionline / falken20
# url_shortener/main.py

# FastAPI creates documentation of your API endpoints for you.
# Go check it out in your browser at:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

import secrets
from fastapi import FastAPI, HTTPException, Depends, Request
import validators  # To validate URLs, email addresses, IP addresses, etc.
from sqlalchemy.orm import Session

from . import schemas, models
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)  # If not exists it'll be created

# It will create and yield new database sessions with each request


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
@app.get("/home")
def main():
    return "Welcome to the URL Shortener API \nThese are the endpoints:"


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    # With get_db() into Depends(), you establish a database session
    # for the request and close the session when the request is finished.
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    # Add key and secret_key to db_url to match the required URLInfo schema
    # that you need to return at the end of the function.
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url
