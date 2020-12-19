from faker import Faker
from src.data.test import PetRepositorySpy
from .register import RegisterPet

faker = Faker()


def test_registry():
    """ Testing registry method in RegisterPet """

    pet_repo = PetRepositorySpy()
    registry_pet = RegisterPet(pet_repo)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_id": faker.random_number(digits=1),
    }

    response = registry_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_id=attributes["user_id"],
    )

    # Testing Inputs
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    assert pet_repo.insert_pet_param["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]
    assert pet_repo.insert_pet_param["user_id"] == attributes["user_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_registry_fail():
    """ Testing registry fail method in RegisterPet """

    pet_repo = PetRepositorySpy()
    registry_pet = RegisterPet(pet_repo)

    attributes = {
        "name": faker.name(),
        "specie": faker.random_number(),
        "age": faker.name(),
        "user_id": faker.random_number(digits=1),
    }

    response = registry_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_id=attributes["user_id"],
    )

    # Testing Inputs
    assert pet_repo.insert_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
