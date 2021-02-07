from typing import Type
from src.data import FindUser
from src.presentation.helpers import HttpRequest, HttpResponse
from src.presentation.errors import HttpErrors


class FindUserRouter:
    """ Class to Define Route to find_user use case """

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]):
        """ Method to call use case """

        response = None

        if http_request.query:
            # if query in http_request

            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_id_and_user(
                    user_id=user_id, name=user_name
                )

            elif (
                "user_id" in query_string_params
                and "user_name" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_user_use_case.by_id(user_id=user_id)

            elif (
                "user_name" in query_string_params
                and "user_id" not in query_string_params
            ):
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_name(name=user_name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
