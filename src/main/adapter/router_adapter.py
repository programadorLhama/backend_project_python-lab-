from typing import Type
from src.presentation.helpers import HttpRequest
from src.main.interface import RouteInterface as Route

def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """ Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    http_request = HttpRequest (
        header=request.headers,
        body=request.json,
        # request.args.to_dict()
        query={
            'user_id': int(request.args.get('user_id'))
        }
    )

    response = api_route.route(http_request)
    return response
