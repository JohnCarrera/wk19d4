import os
from flask_wtf.csrf import  generate_csrf
from flask import Flask, jsonify
from flask_migrate import Migrate


from .config import Configuration
from .utils import ValidationError
from .routes import pokemon
from .routes import items


app = Flask(__name__)


app.config.from_object(Configuration)
app.register_blueprint(pokemon.bp, url_prefix='/api/pokemon')
app.register_blueprint(items.bp, url_prefix='/api/items')

from .models import db

db.init_app(app)
migrate = Migrate(app, db)


# testing the home page route: /
@app.route("/")
def index():
    return "<h1>The server is live!</h1>"

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status
    return response.to_dict()

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
