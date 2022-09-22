# by Richi Rod AKA @richionline / falken20
# url_shortener/main.py

# FastAPI creates documentation of your API endpoints for you. 
# Go check it out in your browser at: 
# http://127.0.0.1:8000/docs 
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/home")
def main():
    return "Welcome to the URL Shortener API"