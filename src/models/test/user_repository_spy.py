from typing import List
from src.models.interfaces import UserRepositoryInterface
from src.models.entities import Users
from .mock_user import mock_users


class UserRepositorySpy(UserRepositoryInterface):
    """ Spy to User Repository """

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_users()

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:

        self.select_user_params["user_id"] = user_id
        self.select_user_params["name"] = name

        return [mock_users()]
