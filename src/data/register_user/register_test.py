from faker import Faker
from src.data.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_registry():
    """ Testing registry method in RegisterUser """

    user_repo = UserRepositorySpy()
    registry_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.word(),
    }

    response = registry_user.registry(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing Inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_registry_fail():
    """ Testing registry fail method in RegisterUser """

    user_repo = UserRepositorySpy()
    registry_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(digits=3),
        "password": faker.word(),
    }

    response = registry_user.registry(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing Inputs
    assert user_repo.insert_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
