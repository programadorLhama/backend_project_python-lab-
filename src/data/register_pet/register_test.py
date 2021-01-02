from faker import Faker
from src.data.test import PetRepositorySpy, UserRepositorySpy, FindUserMock
from .register import RegisterPet

faker = Faker()


def test_registry():
    """ Testing registry method in RegisterPet """

    pet_repo = PetRepositorySpy()
    find_user = FindUserMock(UserRepositorySpy())
    registry_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=1),
            "user_name": faker.name(),
        },
    }

    response = registry_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing Inputs
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    assert pet_repo.insert_pet_param["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]
    assert (
        pet_repo.insert_pet_param["user_id"]
        == attributes["user_information"]["user_id"]
    )

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_registry_fail_attributes():
    """ Testing registry fail method in RegisterPet by attributes """

    pet_repo = PetRepositorySpy()
    find_user = FindUserMock(UserRepositorySpy())
    registry_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.random_number(),
        "age": faker.name(),
        "user_information": {
            "user_id": faker.random_number(digits=1),
            "user_name": faker.name(),
        },
    }

    response = registry_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing Inputs
    assert pet_repo.insert_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_registry_fail_user():
    """ Testing registry fail method in RegisterPet by user search """

    pet_repo = PetRepositorySpy()
    find_user = FindUserMock(UserRepositorySpy())
    registry_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=1),
            "user_name": faker.random_number(),
        },
    }

    response = registry_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing Inputs
    assert pet_repo.insert_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
