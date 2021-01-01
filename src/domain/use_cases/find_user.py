from abc import ABC, abstractmethod
from typing import Dict


class FindUser(ABC):
    """ Interface to FindPet use case """

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[str, str]:
        """ Specific case """

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_name(self, name: str) -> Dict[str, str]:
        """ Specific case """

        raise Exception("Should implement method: by_name")

    @abstractmethod
    def by_id_and_user(self, user_id: int, name: str) -> Dict[str, str]:
        """ Specific case """

        raise Exception("Should implement method: by_id_and_user")
