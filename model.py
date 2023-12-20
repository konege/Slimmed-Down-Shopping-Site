from flask_sqlalchemy import SQLAlchemy
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_no = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Product {self.product_no}>'
