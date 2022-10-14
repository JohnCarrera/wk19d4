from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

types = [
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
    ]
class PokemonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = IntegerField('Number', validators=[DataRequired()])
    attack = IntegerField('Attack', validators=[DataRequired()])
    defense = IntegerField('Defense', validators=[DataRequired()])
    type = SelectField('Type', choices=types, validators=[DataRequired()])
    image_url = StringField('Image Url')
    move1 = StringField('Move 1', validators=[DataRequired()])
    move2 = StringField('Move 2', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    happiness = IntegerField('Happiness', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
