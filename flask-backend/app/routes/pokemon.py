from flask import Blueprint, redirect, jsonify, request
from app import ValidationError
from ..forms import ItemForm, PokemonForm
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
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        pokemon = Pokemon(
            number= data['number'],
            attack= data['attack'],
            defense= data['defense'],
            image_url= data['image_url'] or '/static/images/unknown.png',
            name= data['name'],
            type= data['type'],
            moves= f'{data["move1"]},{data["move2"]}',
        )
        db.session.add(pokemon)
        db.session.commit()
        return jsonify(pokemon.to_dict())
    raise ValidationError('Validation Error')

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
    returnStr=f'updated pokemon {id}'
    return returnStr
