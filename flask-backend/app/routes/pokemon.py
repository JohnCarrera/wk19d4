from flask import Blueprint, redirect, jsonify
from ..models import db, Pokemon, Items

bp = Blueprint("pokemon", __name__)

# routes to /pokemon
@bp.route("", methods=['GET'])
def get_pokemon():
    pokemon = Pokemon.query.all()
    return jsonify([mon.to_dict() for mon in pokemon])

@bp.route("", methods=['POST'])
def create_pokemon():
    return "NEW POKEMON CREATED"

@bp.route("/types")
def get_pokemon_types():
    types = db.session.query(Pokemon.type).distinct().all()
    return jsonify([type[0] for type in types])

    # return jsonify([
    #     "fire",
    #     "electric",
    #     "normal",
    #     "ghost",
    #     "psychic",
    #     "water",
    #     "bug",
    #     "dragon",
    #     "grass",
    #     "fighting",
    #     "ice",
    #     "flying",
    #     "poison",
    #     "ground",
    #     "rock",
    #     "steel"
    # ])

@bp.route("/<int:id>/items")
def get_pokemon_items_id(id):
    pokemon = Pokemon.get(id)
    items = pokemon.items()
    list_items = [item.to_dict for item in items]
    return list_items

@bp.route("/<int:id>/items", methods=['POST'])
def add_pokemon_item_id(id):
    returnStr=f'added item for pokemon {id}'
    return returnStr

@bp.route("/<int:id>")
def get_pokemon_id(id):
    pokemon = Pokemon.get(id)
    return pokemon.to_dict()

@bp.route("/<int:id>", methods=['PUT'])
def update_pokemon_id(id):
    returnStr=f'updated pokemon {id}'
    return returnStr
