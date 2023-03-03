from app import app
from flask import render_template
from models import Product, Color

colors = ['black', 'yellow', 'purple']


@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/product-list")
def productList():
    products = Product.query.all()
    return render_template('product-list.html', products = products)


@app.route("/product-detail/<int:id>/")
def product(id):
    product = Product.query.filter_by(id = id).first()
    colors = Color.query.all()
    return render_template('product-detail.html', item = product, colors = colors)



@app.route("/contact")
def contact():
    return render_template('contact.html')