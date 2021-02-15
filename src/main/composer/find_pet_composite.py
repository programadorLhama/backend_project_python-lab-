from src.presentation import FindPetRouter
from src.data import FindPet
from src.infra import PetRepository


def find_pet_composer() -> FindPetRouter:
    ''' Composing Find Pet Route
    :param - None
    :return - Object with Find Pet Route
    '''

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_router = FindPetRouter(use_case)

    return find_pet_router
