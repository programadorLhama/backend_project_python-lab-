from flask import jsonify, Blueprint, request
from src.main.adapter import flask_adapter
from src.main.composer import find_user_composer

api_routes_bp = Blueprint('api_routes', __name__)

@api_routes_bp.route("/api/getUser", methods=["GET"])
def get_user():
    ''' docstring '''
    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    for count, element in enumerate(response.body):
        message[count] = {'id': element.id, 'name': element.name}

    return jsonify({
        'message': message
    }), response.status_code
