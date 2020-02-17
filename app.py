from flask import Flask
from flask import render_template

import db

app = Flask(__name__)

@app.route('/')
def home():  # CONTROLLER

    # MODEL
    products = db.load_database()

    # VIEW
    html = render_template('home.html', products=products)

    return html


if __name__ == "__main__":
    app.run()