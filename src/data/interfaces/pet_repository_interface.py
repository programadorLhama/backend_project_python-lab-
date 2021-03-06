from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """ Interface to Pet Repository """

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """ Insert data in pets entity """

        raise Exception("Should implement method: insert_pet")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """ Select data in pets entity """

        raise Exception("Should implement method: select_pet")
