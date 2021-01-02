from typing import Dict, List
from src.domain.models import Users
from src.domain.test import mock_users


class FindUserMock:
    """ Class to define usecase: Select User """

    def __init__(self, user_repository: any):
        self.user_repository = user_repository

    @classmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """ Select User By id """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = {"Success": validate_entry, "Data": [mock_users()]}

        return {"Success": validate_entry, "Data": response}

    @classmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """ Select User By name """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = {"Success": validate_entry, "Data": [mock_users()]}

        return {"Success": validate_entry, "Data": response}

    @classmethod
    def by_id_and_user(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """ Select User By id and name """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = {"Success": validate_entry, "Data": [mock_users()]}

        return {"Success": validate_entry, "Data": response}
