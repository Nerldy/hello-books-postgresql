from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
---------------------
---- CONFIG ----
---------------------
"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
app.url_map.strict_slashes = False
db = SQLAlchemy(app)

"""
---------------------
---- BLUEPRINTS ----
---------------------
"""
from app.books.views import books_blueprint
from app.users.views import users_blueprint

# Register Blueprints
app.register_blueprint(books_blueprint)
app.register_blueprint(users_blueprint)
