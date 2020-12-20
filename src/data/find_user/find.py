from typing import Dict, Type
from src.models import UserRepository


class FindUser:
    """ Class to define usecase: Select User """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[str, str]:
        """Select User By id
        :param - user_id: id of the user
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[str, str]:
        """Select User By name
        :param - name: name of the user
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}
