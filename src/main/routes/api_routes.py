from flask import jsonify, Blueprint, request
from src.main.adapter import flask_adapter
from src.main.composer import (
    find_user_composer,
    find_pet_composer,
    register_user_composer,
    register_pet_composer,
)

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


@api_routes_bp.route("/api/getPet", methods=["GET"])
def get_pet():
    """ get pet route """

    message = {}
    response = flask_adapter(request=request, api_route=find_pet_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        for count, element in enumerate(response.body):
            message[count] = {
                "id": element.id,
                "name": element.name,
                "specie": element.specie.value,
            }

        return jsonify({"message": message}), response.status_code

    # Handling Errors
    return jsonify({"message": response.body["error"]}), response.status_code


@api_routes_bp.route("/api/registerUser", methods=["POST"])
def register_user():
    """ register user route """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())
    print(response)

    if response.status_code < 300:
        # If not error, format the message and return it

        message["0"] = {"id": response.body.id, "name": response.body.name}

        return jsonify({"message": message}), response.status_code

    # Handling Errors
    return jsonify({"message": response.body["error"]}), response.status_code


@api_routes_bp.route("/api/registerPet", methods=["POST"])
def register_pet():
    """ register pet route """

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())
    print(response)

    if response.status_code < 300:
        # If not error, format the message and return it

        message["0"] = {
            "id": response.body.id,
            "name": response.body.name,
            "specie": response.body.specie,
        }

        return jsonify({"message": message}), response.status_code

    # Handling Errors
    return jsonify({"message": response.body["error"]}), response.status_code
