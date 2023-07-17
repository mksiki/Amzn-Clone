from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#addpassword@localhost:5434/amazon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from amazon.amzn_models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from amazon.api import users, products, orders
    app.register_blueprint(users.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(orders.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()