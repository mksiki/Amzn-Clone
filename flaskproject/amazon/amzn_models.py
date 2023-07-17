from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate()
db =SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)    
    email = db.Column(db.String(75), unique=True, nullable=False)
    address = db.Column(db.Text, nullable=False)
    user_orders = db.relationship('Order', backref='User')

    def __init__(self, name: str, password: str, email: str, address: str,):
            self.name = name
            self.password = password
            self.email = email
            self.address = address

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, description: str, price: int):
         self.name = name
         self.description = description
         self.price = price 

    def serialize(self):
         return{
              'id': self.id,
              'name': self.name,
              'description': self.description,
              'price': self.price
         }


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cost = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, cost: int, user_id: int, product_id: int):
        self.cost = cost
        self.user_id = user_id
        self.product_id = product_id
    
    def serialize(self):
        return{
            'id': self.id,
            'cost': self.cost,
            'product_id': self.product_id,
            'user_id': self.user_id
        }
