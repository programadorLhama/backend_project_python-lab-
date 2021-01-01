from abc import ABC, abstractmethod
from typing import Dict


class RegisterUser(ABC):
    """ Interface to FindPet use case """

    @abstractmethod
    def registry(self, name: str, password: str) -> Dict[str, str]:
        """ Case """

        raise Exception("Should implement method: registry")
