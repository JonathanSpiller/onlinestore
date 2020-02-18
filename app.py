from flask import Flask, redirect
from flask import render_template

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def home():  # CONTROLLER
    return render_template('home.html')



@app.route('/products')
def products():  # CONTROLLER

    # MODEL
    products = db.load_database()

    # VIEW
    return render_template('products.html', products=products)


@app.route('/product_details/<int:product_id>')
def product_details(product_id):  # CONTROLLER

    # MODEL
    products = db.load_database()


    # VIEW
    return render_template('product_details.html', product=products[product_id])


@app.route('/buy/<int:product_id>')
def buy(product_id):  # CONTROLLER

    # MODEL
    products = db.load_database()
    products[product_id]['stock'] -= 1
    db.update_database(products)

    return redirect(f'/product_details/{product_id}')


















from flask import request
from forms import *

@app.route('/login', methods=('GET', 'POST'))
def login():

    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=login_form)


    if request.method == 'POST' and login_form.validate():
        name = login_form.name.data
        password = login_form.password.data
        info = login_form.info.data

        if name == "Jonathan" and password == "horse":
            return f"<h1>Welcome Jon. Your info is {info}.</h1>"
        else:
            return "<h1>Access Denied</h1>"

    else:
        return "<h1>Failed Validation</h1>"



if __name__ == "__main__":
    app.run()