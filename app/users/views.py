from flask import jsonify, Blueprint

users_blueprint = Blueprint("users", __name__, url_prefix='/api/v1/auth')


@users_blueprint.route('/register')
def register():
	return jsonify({"message": "register new user"})
