from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    last_name = db.Column(db.String(100))
    blogs = db.relationship('Blog', backref = 'user')

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image = db.Column(db.String(100))

    def __init__(self, title, description, price, image):
        self.title = title
        self.description = description
        self.price = price
        self.image = image

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Color(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(100), nullable = True)
    company = db.Column(db.String(100), nullable = True)
    message = db.Column(db.String(255), nullable = True)
    is_subscribe = db.Column(db.Boolean)
    
    def __init__(self, name, email, company, message, is_subscribe):
        self.name = name
        self.email = email
        self.company = company
        self.message = message
        self.is_subscribe = is_subscribe

    def __repr__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()