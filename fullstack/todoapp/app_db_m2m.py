from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Welcome1@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

order_items = db.Table(
    'order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key = True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key = True)
)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(), nullable = False)
    products = db.relationship(
        'Product',
        secondary = order_items,
        backref = db.backref('orders', lazy = True)    
    )

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)


if __name__ == '__main__':
    app.run(host='0.0.0.', port=5000, debug=True)