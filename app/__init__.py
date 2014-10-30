import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)

# Add config file
app.config.from_object('config')

# Define db object
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
# Flask-Login needs to know what view logs users in
lm.login_view = 'login'
# Need a path tmp
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models