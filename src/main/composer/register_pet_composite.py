from src.presentation import RegisterPetRoute
from src.data import RegisterPet, FindUser
from src.infra import PetRepository, UserRepository


def register_pet_composer() -> RegisterPetRoute:
    ''' Composing Register Pet Route
    :param - None
    :return - Object with Register Pet Route
    '''

    repository = PetRepository()
    find_user = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user)
    register_pet_route = RegisterPetRoute(use_case)

    return register_pet_route
