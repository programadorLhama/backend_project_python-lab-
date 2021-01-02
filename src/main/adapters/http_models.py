from typing import Dict


class HttpRequest:
    """ Class to adapt http_request """

    def __init__(self, headers: Dict = None, body: Dict = None, query: Dict = None):
        self.headers = headers
        self.body = body
        self.query = query

    def __repr__(self):
        return f"HttpRequest [headers={self.headers}, body={self.body}, query={self.query}]"


class HttpResponse:
    """ Class to adapt http_response """

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse [StatusCode={self.status_code}, Body={self.body}]"
