from typing import Type
from sqlalchemy.orm.exc import NoResultFound
from src.presentation.helpers import HttpRequest, HttpResponse
from src.presentation.errors import HttpErrors
from src.main.interface import RouteInterface as Route


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        # Query string params
        query_string_params = request.args.to_dict()

        # Formating information
        if "user_id" in query_string_params.keys():
            query_string_params["user_id"] = int(query_string_params["user_id"])
    except:
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=query_string_params
    )

    try:
        response = api_route.route(http_request)

    except NoResultFound:
        https_error = HttpErrors.error_404()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    except:
        https_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    return response
