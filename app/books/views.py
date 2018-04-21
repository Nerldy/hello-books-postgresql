from flask import Blueprint, jsonify

books_blueprint = Blueprint('books', __name__, url_prefix="/api/v1")


@books_blueprint.route('/books')
def index():
	return jsonify({"message": 'Hello Books'})
