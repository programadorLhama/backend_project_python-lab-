from src.presentation import RegisterUserRouter
from src.data import RegisterUser
from src.infra import UserRepository

def register_user_composer() -> RegisterUserRouter:
    ''' Composing Register User Route
    :param - None
    :return - Object with Register User Route
    '''

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserRouter(use_case)

    return register_user_route
