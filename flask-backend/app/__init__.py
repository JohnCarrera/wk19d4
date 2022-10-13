import os
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, render_template, redirect
from .config import Configuration
from flask_migrate import Migrate
from .models import db
from .routes import pokemon
from .routes import items

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon.bp, url_prefix='/api/pokemon')
app.register_blueprint(items.bp, url_prefix='/api/items')

db.init_app(app)
migrate = Migrate(app, db)


# testing the home page route: /
@app.route("/")
def index():
    return "<h1>The server is live!</h1>"


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
