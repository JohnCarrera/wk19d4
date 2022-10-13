from flask import Blueprint, redirect, jsonify, request
from ..forms import ItemForm
from ..models import db, Pokemon, Items

from random import randint


def random_item_image():
    images = ["/static/images/pokemon_berry.svg",
            "/static/images/pokemon_egg.svg",
            "/static/images/pokemon_potion.svg",
            "/static/images/pokemon_super_potion.svg"]

    num = randint(0, len(images) - 1)
    return images[num]


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
    return jsonify([
        "fire",
        "electric",
        "normal",
        "ghost",
        "psychic",
        "water",
        "bug",
        "dragon",
        "grass",
        "fighting",
        "ice",
        "flying",
        "poison",
        "ground",
        "rock",
        "steel"
    ])

@bp.route("/<int:id>/items")
def get_pokemon_items_id(id):
    pokemon = Pokemon.query.get(id)
    items = pokemon.items
    list_items = jsonify([item.to_dict() for item in items])
    return list_items

@bp.route("/<int:id>/items", methods=['POST'])
def add_pokemon_item_id(id):
    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        print(data)
        item = Items(
            name = data['name'],
            happiness = data['happiness'],
            price = data['price'],
            pokemon_id = id,
            image_url = random_item_image()
        )

        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict())
    return

@bp.route("/<int:id>")
def get_pokemon_id(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()

@bp.route("/<int:id>", methods=['PUT'])
def update_pokemon_id(id):

    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        print(data)
        pokemon = Pokemon.query.get(id)
        pokemon.update(item.to_dict())
        db.session.commit()
    returnStr=f'updated pokemon {id}'
    return jsonify(returnStr)
