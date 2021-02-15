from src.presentation import FindUserRouter
from src.data import FindUser
from src.infra import UserRepository


def find_user_composer() -> FindUserRouter:
    ''' Composing Find User Route
    :param - None
    :return - Object with Find User Route
    '''

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserRouter(use_case)

    return find_user_route
