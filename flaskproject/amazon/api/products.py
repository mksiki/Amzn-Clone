from flask import Blueprint, jsonify, abort, request
from amazon.amzn_models import Product, db


bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('', methods=['GET'])
def index():
    products = Product.query.all()
    result = []
    for o in products:
        result.append(o.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    o = Product.query.get_or_404(id)
    return jsonify(o.serialize())