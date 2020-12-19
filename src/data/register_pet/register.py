from typing import Tuple


class RegisterPet:
    """ Class to define usecase: Register Pet """

    def __init__(self, PetRepository):
        self.pet_repository = PetRepository()

    def registry(self, name, specie, age, user_id) -> Tuple[int, str, str, int, int]:
        """Registry pet
        :param  - name: person name
                - specie: Enum with species acepted
                - age: age of the pet
                - user_id: id of the owner (FK)
        :return - tuple with new pet inserted informations
        """

        response = self.pet_repository.insert_pet(name, specie, age, user_id)
        success = (
            (response.name is name)
            and (response.specie is specie)
            and (response.age is age)
            and (response.user_id is user_id)
        )

        return {"Success": success, "Data": response}
