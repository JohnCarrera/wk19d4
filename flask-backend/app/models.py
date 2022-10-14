from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
  __tablename__ = 'pokemon'

  id = db.Column(db.Integer,  primary_key=True)
  number = db.Column(db.Integer, nullable=False)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.VARCHAR, nullable=False)
  name = db.Column(db.VARCHAR, nullable=False, unique=True)
  type = db.Column(db.VARCHAR, nullable=False)
  moves = db.Column(db.VARCHAR, nullable=False)
  encounter_rate = db.Column(db.Float(precision=3), default=1)
  catch_rate = db.Column(db.Float(precision=3), default=1)
  captured = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default=dt.now())
  updated_at = db.Column(db.DateTime, default=dt.now())

  items = db.relationship('Items', back_populates='pokemon')

  def to_dict(self):
    return {
      'id': self.id,
      'number': self.number,
      'attack': self.attack,
      'defense': self.defense,
      'imageUrl': self.image_url,
      'name': self.name,
      'type': self.type,
      'moves': self.moves.split(','),
      'encounterRate': self.encounter_rate,
      'catchRate': self.catch_rate,
      'captured': self.captured,
      'createdAt': self.created_at,
      'updatedAt': self.updated_at,
    }

class Items(db.Model):
  __tablename__ = 'items'

  id = db.Column(db.Integer, primary_key=True)
  happiness = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.VARCHAR, nullable=False)
  name = db.Column(db.VARCHAR, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
  created_at = db.Column(db.DateTime, default=dt.now())
  updated_at = db.Column(db.DateTime, default=dt.now())

  pokemon = db.relationship('Pokemon', back_populates='items')

  def to_dict(self):
    return {
      'id': self.id ,
      'happiness': self.happiness ,
      'imageUrl': self.image_url ,
      'name': self.name ,
      'price': self.price ,
      'pokemonId': self.pokemon_id ,
      'createdAt': self.created_at ,
      'updatedAt': self.updated_at ,
    }
