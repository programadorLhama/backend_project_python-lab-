from flask import jsonify, Blueprint, request
from src.main.adapter import flask_adapter
from src.main.composer import (
    find_user_composer,
    find_pet_composer,
    register_user_composer,
    register_pet_composer,
)

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["GET"])
def get_user():
    """ get user route """

    response = flask_adapter(request=request, api_route=find_user_composer())

    message = []
    if response.status_code < 300:
        # If not error, format the message and return it

        for element in response.body:
            message.append(
                {
                    "type": "Users",
                    "id": element.id,
                    "attributes": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets/", methods=["GET"])
def get_pet():
    """ get pet route """

    response = flask_adapter(request=request, api_route=find_pet_composer())

    message = []
    if response.status_code < 300:
        # If not error, format the message and return it

        for element in response.body:
            message.append(
                {
                    "type": "Pets",
                    "id": element.id,
                    "attributes": {
                        "name": element.name,
                        "specie": element.specie.value,
                        "age": element.age,
                    },
                    "relationships": {
                        "Owner": {"type": "Users", "id": element.user_id}
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """ register user route """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        message = {
            "type": "Users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pet():
    """ register pet route """

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())
    print(response)

    if response.status_code < 300:
        # If not error, format the message and return it

        message = {
            "type": "Pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"Owner": {"type": "Users", "id": response.body.user_id}},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )
