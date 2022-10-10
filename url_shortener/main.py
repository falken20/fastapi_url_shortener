# by Richi Rod AKA @richionline / falken20
# url_shortener/main.py

# FastAPI creates documentation of your API endpoints for you.
# Go check it out in your browser at:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
import validators  # To validate URLs, email addresses, IP addresses, etc.
from sqlalchemy.orm import Session

from . import schemas, models, crud
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

    db_url = crud.create_db_url(db=db, url=url)
    # Add key and secret_key to db_url to match the required URLInfo schema
    # that you need to return at the end of the function.
    db_url.url = db_url.key
    db_url.admin_url = db_url.secret_key

    return db_url


@app.get("/{url_key}")
def forward_to_target_url(url_key: str, request: Request, db: Session = Depends(get_db)):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
