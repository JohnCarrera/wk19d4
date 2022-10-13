from random import randint
from app.models import db, Items, Pokemon
from app import app

with app.app_context():

    pokemon_seed = [{
        'number': 1,
        'image_url': '/static/images/pokemon_snaps/1.svg',
        'name': 'Bulbasaur',
        'attack': 49,
        'defense': 49,
        'type': 'grass',
        'moves': ','.join([
            'tackle',
            'vine whip'
        ]),
        'captured': True
    },
    {
        'number': 2,
        'image_url': '/static/images/pokemon_snaps/2.svg',
        'name': 'Ivysaur',
        'attack': 62,
        'defense': 63,
        'type': 'grass',
        'moves': ','.join([
            'tackle',
            'vine whip',
            'razor leaf'
        ]),
        'captured': True
    },
    {
        'number': 3,
        'image_url': '/static/images/pokemon_snaps/3.svg',
        'name': 'Venusaur',
        'attack': 82,
        'defense': 83,
        'type': 'grass',
        'moves': ','.join([
            'tackle',
            'vine whip',
            'razor leaf'
        ]),
        'captured': True
    },
    {
        'number': 4,
        'image_url': '/static/images/pokemon_snaps/4.svg',
        'name': 'Charmander',
        'attack': 52,
        'defense': 43,
        'type': 'fire',
        'moves': ','.join([
            'scratch',
            'ember',
            'metal claw'
        ]),
        'captured': True
    },
    {
        'number': 5,
        'image_url': '/static/images/pokemon_snaps/5.svg',
        'name': 'Charmeleon',
        'attack': 64,
        'defense': 58,
        'type': 'fire',
        'moves': ','.join([
            'scratch',
            'ember',
            'metal claw',
            'flamethrower'
        ]),
        'captured': True
    },
    {
        'number': 6,
        'image_url': '/static/images/pokemon_snaps/6.svg',
        'name': 'Charizard',
        'attack': 84,
        'defense': 78,
        'type': 'fire',
        'moves': ','.join([
            'flamethrower',
            'wing attack',
            'slash',
            'metal claw'
        ]),
        'captured': True
    },
    {
        'number': 7,
        'image_url': '/static/images/pokemon_snaps/7.svg',
        'name': 'Squirtle',
        'attack': 48,
        'defense': 65,
        'type': 'water',
        'moves': ','.join([
            'tackle',
            'bubble',
            'water gun'
        ]),
        'captured': True
    },
    {
        'number': 8,
        'image_url': '/static/images/pokemon_snaps/8.svg',
        'name': 'Wartortle',
        'attack': 63,
        'defense': 80,
        'type': 'water',
        'moves': ','.join([
            'tackle',
            'bubble',
            'water gun',
            'bite'
        ]),
    },
    {
        'number': 9,
        'image_url': '/static/images/pokemon_snaps/9.svg',
        'name': 'Blastoise',
        'attack': 83,
        'defense': 100,
        'type': 'water',
        'moves': ','.join([
            'hydro pump',
            'bubble',
            'water gun',
            'bite'
        ]),
    },
    {
        'number': 10,
        'image_url': '/static/images/pokemon_snaps/10.svg',
        'name': 'Caterpie',
        'attack': 30,
        'defense': 35,
        'type': 'bug',
        'moves': ','.join([
            'tackle'
        ]),
    },
    {
        'number': 12,
        'image_url': '/static/images/pokemon_snaps/12.svg',
        'name': 'Butterfree',
        'attack': 45,
        'defense': 50,
        'type': 'bug',
        'moves': ','.join([
            'confusion',
            'gust',
            'psybeam',
            'silver wind'
        ]),
    },
    {
        'number': 13,
        'image_url': '/static/images/pokemon_snaps/13.svg',
        'name': 'Weedle',
        'attack': 35,
        'defense': 30,
        'type': 'bug',
        'moves': ','.join([
            'poison sting'
        ]),
    },
    {
        'number': 16,
        'image_url': '/static/images/pokemon_snaps/16.svg',
        'name': 'Pidgey',
        'attack': 45,
        'defense': 40,
        'type': 'normal',
        'moves': ','.join([
            'tackle',
            'gust'
        ]),
    },
    {
        'number': 17,
        'image_url': '/static/images/pokemon_snaps/17.svg',
        'name': 'Pidgeotto',
        'attack': 60,
        'defense': 55,
        'type': 'normal',
        'moves': ','.join([
            'tackle',
            'gust',
            'wing attack'
        ]),
    },
    {
        'number': 18,
        'image_url': '/images/pokemon_snaps/18.svg',
        'name': 'Pidgeot',
        'attack': 80,
        'defense': 75,
        'type': 'normal',
        'moves': ','.join([
          'tackle',
          'gust',
          'wing attack'
        ]),
    }]

    def generate_pokemon(seed_data):
        pokemon = []
        for seed in seed_data:
            pokemon.append(Pokemon(**seed))

        return pokemon

    def random_item_image():
        images = ["/static/images/pokemon_berry.svg",
                "/static/images/pokemon_egg.svg",
                "/static/images/pokemon_potion.svg",
                "/static/images/pokemon_super_potion.svg"]

        num = randint(0, len(images) - 1)
        return images[num]

    def random_item_name():
        names = [ "Unbranded Fresh Keyboard",
                "Generic Concrete Pizza",
                "Tasty Cotton Computer",
                "Fantastic Steel Shirt",
                "Practical Soft Car",
                "Fantastic Plastic Bacon",
                "Gorgeous Frozen Pizza",
                "Licensed Wooden Hat",
                "Gorgeous Steel Salad",
                "Awesome Wooden Table",
                "Small Frozen Keyboard",
                "Rustic Metal Computer"]

        num = randint(0, len(names) - 1)
        return names[num]

    def generate_items(pokemon_lst):
        items = []
        for pokemon in pokemon_lst:
            for i in range(0, 3):
                items.append(Items(pokemon=pokemon,
                    price=randint(1, 100),
                    happiness=randint(1, 100),
                    image_url=random_item_image(),
                    name=random_item_name()))

        return items

    pokemon_lst = generate_pokemon(pokemon_seed)

    items = generate_items(pokemon_lst)

    for pokemon in pokemon_lst:
        db.session.add(pokemon)

    db.session.commit()