from typing import Dict, Type
from src.models.repositorys import PetRepository


class RegisterPet:
    """ Class to define usecase: Register Pet """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def registry(self, name, specie, age, user_id) -> Dict[str, str]:
        """Registry pet
        :param  - name: person name
                - specie: Enum with species acepted
                - age: age of the pet
                - user_id: id of the owner (FK)
        :return - tuple with new pet inserted informations
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and isinstance(age, int)
            and isinstance(user_id, int or None)
        )

        if validate_entry:
            response = self.pet_repository.insert_pet(name, specie, age, user_id)

        return {"Success": validate_entry, "Data": response}
