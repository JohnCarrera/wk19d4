################# INSTALL PACKAGES #################
pipenv install pycodestyle pylint rope flask flask-sqlalchemy alembic flask-migrate python-dotenv sqlalchemy wtforms flask-wtf
echo '=> Finished installing packages'
####################################################


################# CREATE ENV FILES #################
touch .flaskenv
echo 'FLASK_APP=app' >> .flaskenv
echo 'FLASK_DEBUG=True' >> .flaskenv
echo "=> Finished creating .flaskenv"
touch .env
echo 'SECRET_KEY=<<ADD_SECRET_KEY_HERE>>' >> .env
echo "DATABASE_URL='sqlite:///dev.db'" >> .env
echo "=> Finished creating .env"
####################################################


################# CREATE APP FILES #################
mkdir app
cd app

#
touch __init__.py
echo '''from flask import Flask, render_template, redirect
from .config import Configuration
from flask_migrate import Migrate
from .models import db
from .routes import test

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(test.bp)

db.init_app(app)
migrate = Migrate(app, db)


# testing the home page route: /
@app.route("/")
def index():
    return "<h1>The server is live!</h1>"''' >> __init__.py
echo "=> Finished creating __init__.py"


touch config.py
echo '''from os import environ

class Configuration():
    SECRET_KEY=environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI=environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
''' >> config.py
echo "=> Finished creating config.py"

touch forms.py
echo '''from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired''' >> forms.py
echo "=> Finished creating forms.py"


touch models.py
echo '''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()''' >> models.py
echo "=> Finished creating models.py"
####################################################


########## CREATE ROUTES, TEMPLATES FILES ##########
mkdir routes
mkdir templates
echo "=> Finished creating the following directories: routes, templates"


cd routes
touch __init__.py
touch test.py
echo '''from flask import Blueprint, render_template, redirect
from ..models import db

bp = Blueprint("test", __name__, url_prefix="/test")

# routes to /test
@bp.route("/")
def test():
    return "<h1>Test Route</h1>"''' >> test.py
echo "=> Added __init__.py and test.py in routes directory"


cd ..


cd templates
touch index.html
echo '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>''' >> index.html
echo "=> Added index.html in templates directory"
####################################################


##################### COMPLETE #####################
cd ../..
echo "=> Finished installing flask and creating appropriate directories!"
####################################################
