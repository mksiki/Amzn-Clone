from faker import Faker 
from amazon.amzn_models import User, Order, Product, db
from app import create_app

app = create_app()
fake = Faker()


with app.app_context():
    for _ in range(5):
        user = User(
            name=fake.name(),
            password=fake.password(),
            email=fake.email(),
            address=fake.address()
        )
        db.session.add(user)
    db.session.commit()

    for _ in range(40):
        product = Product(
            name=fake.word(),
            description=fake.sentence(),
            price=fake.random_int(min=5, max=1000)     
        )
        db.session.add(product)
    db.session.commit()

    for _ in range(10):
        order = Order(
            cost=fake.random_int(min=5, max=1000),
            product_id=fake.random_int(min=1, max=80), 
            user_id=fake.random_int(min=1, max=20)
        )
        db.session.add(order)
    db.session.commit()

    users = User.query.all()
    products = Product.query.all()
    orders = Order.query.all()
            
