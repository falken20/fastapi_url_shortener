#!/bin/sh

echo "Create virtual environment..."
#python -m venv venv

echo "Access to virtual environment..."
#source ./venv/bin/activate

echo "Running app...uvicorn url_shortener.main:app --reload"
# The --reload flag makes sure that your server will reload automatically when you save your application’s code
uvicorn url_shortener.main:app --reload

echo "Deactivate virtual environment..."
#deactivate