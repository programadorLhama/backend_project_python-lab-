from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """ Interface to FindPet use case """

    @abstractmethod
    def registry(self, name: str, password: str) -> Dict[bool, Users]:
        """ Case """

        raise Exception("Should implement method: registry")
