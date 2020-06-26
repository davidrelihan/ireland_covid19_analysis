# Setting up Dashand publish to heroku
Followed guide https://dash.plotly.com/deployment

```
$ virtualenv venv # creates a virtualenv called "venv"
$ .\venv\Scripts\activate # uses the virtualenv
$ pip install dash
$ pip install plotly
$ pip install gunicorn

Create the following files in your project folder: app.py

.gitignore

venv
*.pyc
.DS_Store
.env

Procfile

web: gunicorn app:server
(Note that app refers to the filename app.py. server refers to the variable server inside that file).


pip freeze > requirements.txt
```