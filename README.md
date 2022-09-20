<div align="center">
  
<img src="./static/assets/logo_app.png" alt="drawing" width="400"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://falken-home.herokuapp.com/static/home_project/img/falken_logo.png" width=40 alt="Personal Portfolio web"></a>

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/url_shortener) ![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/url_shortener) ![Test coverage](https://img.shields.io/badge/test%20coverage-0%25-green) ![GitHub License](https://img.shields.io/github/license/falken20/url_shortener)
  
[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) [![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)

Optionals:
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org) 
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/falken20/primazon?logo=python&logoColor=white)
[![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)
![Tag](https://img.shields.io/badge/tag-1.0.0-blue) 
![Release](https://img.shields.io/badge/release-1.0.0-blue)
</div>

---
# url_shortener
API service in FastAPI to get shortener urls

##### Deploy
```bash
Explain Heroku, GCP, etc. deploy method
```

##### Setup
```bash
pip install -r requirements.txt
```

##### Running the app
```bash
cd falken_chat
python main.py
```

##### Setup tests
```bash
pip install -r requirements-tests.txt
```

##### Running the tests with pytest and coverage
```bash
./scripts/ccheck_project.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/tests/*
```

##### Environment vars
```bash
ENV_PRO=N
LOG_LEVEL=INFO

# Weather station API key
API_KEY=XXXXXXXXXXXX
STATION_ID=XXXXXXXXXXXX

# Twitter params
CONSUMER_KEY=XXXXXXXXXXXX
CONSUMER_SECRET=XXXXXXXXXXXX
ACCESS_TOKEN=XXXXXXXXXXXX
ACCESS_TOKEN_SECRET=XXXXXXXXXXXX
```

---

##### Versions

1.2.0 New Log model integrated

1.1.0 Adaptations to ORM SQLAlchemy
