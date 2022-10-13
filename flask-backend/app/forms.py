from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    attack = IntegerField('Attack', validators=[DataRequired()])
    defense = IntegerField('Defense', validators=[DataRequired()])
    imageUrl = StringField('Image Url', validators=[DataRequired()])
    move1 = StringField('Move 1', validators=[DataRequired()])
    move2 = StringField('Move 2', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    happiness = IntegerField('Happiness', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
