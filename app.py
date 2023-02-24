from flask import Flask, render_template

app = Flask(__name__)


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


@app.route("/home")
def home():
    return render_template('index.html', students  = users)


@app.route("/contact")
def contact():
    return render_template('contact.html')