class HttpErrors:
    """ Class to define http errors """

    @staticmethod
    def error_400():
        """ Http error 400 - Bad Request """

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_404():
        """ Http error 404 - Not Found """

        return {"status_code": 404, "body": {"error": "Not Found"}}

    @staticmethod
    def error_422():
        """ Http error 422 - Unprocessable Entity """

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_500():
        """ Http error 500 - Internal Server Error """

        return {"status_code": 500, "body": {"error": "Internal Server Error"}}
