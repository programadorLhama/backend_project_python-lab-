from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.main.adapters import HttpRequest
from .find_pet_router import FindPetRouter

faker = Faker()


def test_route():
    """ Testing route method in FindPetRouter """

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetRouter(find_pet_use_case)

    http_request = HttpRequest(
        query={
            "pet_id": faker.random_number(digits=2),
            "user_id": faker.random_number(digits=2),
        }
    )

    http_response = find_pet_router.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_pet_id():
    """ Testing route method in FindPetRouter """

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetRouter(find_pet_use_case)

    http_request = HttpRequest(query={"pet_id": faker.random_number(digits=2)})

    http_response = find_pet_router.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_query():
    """ Testing route method in FindPetRouter """

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetRouter(find_pet_use_case)

    http_request = HttpRequest()

    http_response = find_pet_router.route(http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body


def test_route_error_wrong_query():
    """ Testing route method in FindPetRouter """

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetRouter(find_pet_use_case)

    http_request = HttpRequest(query={"something": faker.random_number(digits=2)})

    http_response = find_pet_router.route(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body
