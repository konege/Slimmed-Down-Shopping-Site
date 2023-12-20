from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from model import Product

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    products = Product.query.filter(
        db.or_(
            Product.description.ilike(f'%{query}%'),
            Product.product_no.ilike(f'%{query}%'),
            Product.category.ilike(f'%{query}%')
        )
    ).all()

    return render_template('search.html', products=products, search_query=query)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    db.create_all()  # Creates the database tables

    # Add some products
    if Product.query.count() == 0:
        product1 = Product(product_no='1', description='I LOVE SCHOOL TEE WHITE', price=44.99, image= "i_love_school_tee_white.PNG", category='T-shirt')
        product2 = Product(product_no='2', description='UNIVERSITY TEE BLACK', price=44.99, image= "university_tee_black.PNG", category='T-shirt')
        product3 = Product(product_no='3', description='GUNRANGE HOODIE GREY', price=79.99, image= "gunrange_hoodie_grey.PNG", category='Sweater')
        product4 = Product(product_no='4', description='SHOOTING HOUSE HOODIE BLACK', price=79.99, image= "shooting_house_hoodie_black.PNG", category='Sweater')
        product5 = Product(product_no='5', description='V-LOGO KNITWEAR BLACK', price=79.99, image= "v_logo_knitwear_black.PNG", category='Knitwear')
        product6 = Product(product_no='6', description='V-LOGO KNITWEAR LIGHT GREY', price=79.99, image= "v_logo_knitwear_light_grey.PNG", category='Knitwear')
        product7 = Product(product_no='7', description='420 CARGOPANTS BLACK', price=159.99, image= "420_cargopants_black.PNG", category='Bottoms')
        product8 = Product(product_no='8', description='TRACK PANTS GREY', price=79.99, image= "track_pants_grey.PNG", category='Bottoms')
        product9 = Product(product_no='9', description='AKIMBO LOWS "BLACK PHANTOM"', price=199.99, image= "akimbo_lows_black_phantom.PNG", category='Shoes')
        product10 = Product(product_no='10', description='AKIMBO LOWS "WHITE FOX"', price=199.99, image= "akimbo_lows_white_fox.PNG", category='Shoes')

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)
        db.session.add(product5)
        db.session.add(product6)
        db.session.add(product7)
        db.session.add(product8)
        db.session.add(product9)
        db.session.add(product10)

        db.session.commit()