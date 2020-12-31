from typing import Dict, Type
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUser:
    """ Class to define usecase: Register User """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def registry(self, name: str, password: str) -> Dict[str, str]:
        """Registry user
        :param  - name: person name
                - password: password of the person
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
