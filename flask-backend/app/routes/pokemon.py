from flask import Blueprint, render_template, redirect
from ..models import db

bp = Blueprint("pokemon", __name__)

# routes to /pokemon
@bp.route("", methods=['GET'])
def get_pokemon():
    return "an array of pokemon"

@bp.route("", methods=['POST'])
def create_pokemon():
    return "NEW POKEMON CREATED"

@bp.route("/types")
def get_pokemon_types():
    return "an array of pokemon types"

@bp.route("/<int:id>/items")
def get_pokemon_items_id(id):
    returnStr=f'items for pokemon {id}'
    return returnStr

@bp.route("/<int:id>/items", methods=['POST'])
def add_pokemon_item_id(id):
    returnStr=f'added item for pokemon {id}'
    return returnStr

@bp.route("/<int:id>")
def get_pokemon_id(id):
    returnStr=f'this is pokemon {id}'
    return returnStr

@bp.route("/<int:id>", methods=['PUT'])
def update_pokemon_id(id):
    returnStr=f'updated pokemon {id}'
    return returnStr
