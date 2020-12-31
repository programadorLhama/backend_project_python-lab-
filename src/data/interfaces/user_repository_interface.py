from abc import ABC, abstractmethod
from typing import List
from src.infra.entities import Users


class UserRepositoryInterface(ABC):
    """ Interface to User Repository """

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """ Insert data in user entity """

        raise Exception("Should implement method: insert_user")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """ Select data in user entity """

        raise Exception("Should implement method: select_pet")
