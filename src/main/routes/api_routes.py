from flask import jsonify, Blueprint, request
from src.main.adapter import flask_adapter
from src.main.composer import find_user_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/getUser", methods=["GET"])
def get_user():
    """ get user route """
    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        for count, element in enumerate(response.body):
            message[count] = {"id": element.id, "name": element.name}

        return jsonify({"message": message}), response.status_code

    # Handling Errors
    return jsonify({"message": response.body["error"]}), response.status_code
