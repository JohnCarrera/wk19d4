from flask import Blueprint, render_template, redirect
from ..models import db

bp = Blueprint("test", __name__, url_prefix="/test")

# routes to /test
@bp.route("/")
def test():
    return "<h1>Test Route</h1>"
