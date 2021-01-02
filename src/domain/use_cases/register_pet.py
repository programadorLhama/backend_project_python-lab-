from abc import ABC, abstractmethod
from typing import Dict


class RegisterPet(ABC):
    """ Interface to FindPet use case """

    @abstractmethod
    def registry(
        self, name: str, specie: str, age: int, user_information: Dict[int, str]
    ) -> Dict[str, str]:
        """ Case """

        raise Exception("Should implement method: registry")
