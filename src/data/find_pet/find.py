from typing import Dict, Type
from src.models import PetRepository


class FindPet:
    """ Class to define usecase: Select Pet """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_user_id(self, user_id: int) -> Dict[str, str]:
        """Select Pet By user_id
        :param - user_id: id of the user owne of the pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}
