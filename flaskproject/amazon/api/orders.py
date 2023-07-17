from flask import Blueprint, jsonify, abort, request
from amazon.amzn_models import Order, User, db

bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('', methods=['GET'])
def index():
    orders = Order.query.all()
    result = []
    for o in orders:
        result.append(o.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    o = Order.query.get_or_404(id)
    return jsonify(o.serialize())


@bp.route('', methods=["POST"])
def create():
    if 'user_id' not in request.json or 'product_id' not in request.json:
        return abort(400)
    User.query.get_or_404(request.json['user_id'])
    o = Order(
        user_id=request.json['user_id'],
        product_id=request.json['product_id']
    )

    db.session.add(o)
    db.session.commit()
    return jsonify(o.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    o = Order.query.get_or_404(id)
    try:
        db.session.delete(o)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    