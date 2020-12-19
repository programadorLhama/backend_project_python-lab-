from typing import List
from src.domain.interfaces import PetRepositoryInterface
from src.models.entities import Pets
from src.domain.test import mock_pet


class PetRepositorySpy(PetRepositoryInterface):
    """ Spy to Pet Repository """

    def __init__(self):
        self.insert_pet_param = {}
        self.select_pet = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:

        self.insert_pet_param["name"] = name
        self.insert_pet_param["specie"] = specie
        self.insert_pet_param["age"] = age
        self.insert_pet_param["user_id"] = user_id

        return mock_pet()

    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:

        self.select_pet["pet_id"] = pet_id
        self.select_pet["user_id"] = user_id

        return [mock_pet()]
