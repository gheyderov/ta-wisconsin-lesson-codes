from flask import Flask, render_template

app = Flask(__name__)


colors = ['black', 'yellow', 'purple']

users = {
    'user_1' : {
        'id' : 1,
        'name' : 'John',
        'surname' : 'Doe'
    },
    'user_2' : {
        'id' : 2,
        'name' : 'Kelly',
        'surname' : 'Doe'
    },
    'user_3' : {
        'id' : 3,
        'name' : 'Smith',
        'surname' : 'Doe'
    }
}


products = {
    1 : {
        'id' : 1,
        'title' : 'Product 1',
        'price' : 100,
        'description' : 'some description 1',
        'image' : 'p1.avif'
    },
    2 : {
        'id' : 2,
        'title' : 'Product 2',
        'price' : 200,
        'description' : 'some description 2',
        'image' : 'p2.avif'
    },
    3 : {
        'id' : 3,
        'title' : 'Product 3',
        'price' : 300,
        'description' : 'some description 3',
        'image' : 'p3.avif'
    }
}

@app.route("/home")
def home():
    return render_template('index.html', students  = users)


@app.route("/product-list")
def productList():
    return render_template('product-list.html', products = products)


@app.route("/product-detail/<int:id>/")
def product(id):

    return render_template('product-detail.html', item = products[id], colors = colors)



@app.route("/contact")
def contact():
    return render_template('contact.html')