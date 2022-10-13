from flask import Blueprint, render_template, redirect
from ..models import db, Items

bp = Blueprint("items", __name__)

# routes to /items
@bp.route("/<int:id>", methods=['PUT'])
def update_item_id(id):
    returnStr=f'updated item {id}'
    return returnStr

@bp.route("/<int:id>", methods=['DELETE'])
def delete_item_id(id):

    item = Items.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {'id': id}
