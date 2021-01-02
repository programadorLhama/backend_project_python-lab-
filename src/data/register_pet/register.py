from typing import Dict, Type
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import RegisterPet as RegistryPetInterface
from src.data.find_user import FindUser


class RegisterPet(RegistryPetInterface):
    """ Class to define usecase: Register Pet """

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, age: int, user_information: Dict[int, str]
    ) -> Dict[str, str]:
        """Registry pet
        :param  - name: pet name
                - specie: type of the specie
                - age: age of the pet
                - user_id: id of the owner (FK)
        :return - Dictionary with informations of the process
        """

        response = None

        # Validating entry and trying to find an user
        validate_entry = (
            isinstance(name, str) and isinstance(specie, str) and isinstance(age, int)
        )
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name, specie, age, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(self, user_information: Dict[int, str]):
        """ Check userInfo Dicionaty and select user """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" and "user_name" in user_params:
            # find user by id and name
            user_founded = self.find_user.by_id_and_user(
                user_information["user_id"], user_information["user_name"]
            )

        elif "user_name" not in user_params and "user_id" in user_params:
            # find user by id
            user_founded = self.find_user.by_id(user_information["user_id"])

        elif "user_id" not in user_params and "user_name" in user_params:
            # find user by name
            user_founded = self.find_user.by_name(user_information["user_name"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
