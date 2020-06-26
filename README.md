# ireland_covid19_analysis
[Link to jupyter notebook containing analysis](https://github.com/davidrelihan/ireland_covid19_analysis/blob/master/ireland_c19_analysis.ipynb)

# Setting up Dash and publish to heroku
Create app on https://dashboard.heroku.com/
https://dashboard.heroku.com/apps/ireland-c19-analysis
https://medium.com/@austinlasseter/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73

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

Connect github to heroku app