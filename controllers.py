from app import app
from flask import render_template, request
from models import Product, Color, Contact
from forms import ContactForm

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



@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        print(request.form)
        print('post')
        form = ContactForm(request.form)
        if form.validate_on_submit():
            print('valid')
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                is_subscribe = form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)