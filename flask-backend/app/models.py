from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


db = SQLAlchemy()


class Pokemon(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  number = db.Column(db.Integer, nullable=False)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.VARCHAR, nullable=False)
  name = db.Column(db.VARCHAR, nullable=False, unique=True)
  type = db.Column(db.VARCHAR, nullable=False)
  moves= type = db.Column(db.VARCHAR, nullable=False)
  encounter_rate = db.Column(db.Float(precision=3), default=1)
  catch_rate = db.Column(db.Float(precision=3), default=1)
  captured = db.Column(db.Boolean, default=False)
  updated_at = db.Column(db.DateTime, default=dt.now())
  updated_at = db.Column(db.DateTime, default=dt.now())
