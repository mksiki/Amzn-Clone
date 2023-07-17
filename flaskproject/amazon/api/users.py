from flask import Blueprint, jsonify, request, abort
from amazon.amzn_models import User, db, order_product
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'password' not in request.json:
        return abort(400)
    
    if len(request.json['name']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    u = User(
        name=request.json['name'],
        password=request.json['password'],
        email=request.json['email'],
        address=request.json['address']
    )
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'name' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        u.name = request.json['name']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])


    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
    

@bp.route('/<int:id>/order_product', methods=['GET'])
def liking_users(id: int):
    o_p = User.query.get_or_404(id)
    result = []
    for u in o_p.order_product:
        result.append(u.serialize())
    return jsonify(result)