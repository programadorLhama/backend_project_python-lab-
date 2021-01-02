from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.main.adapters import HttpRequest
from .find_user_router import FindUserRouter

faker = Faker()


def test_route():
    """ Testing route method in FindUserRouter """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_router = FindUserRouter(find_user_use_case)
    attributes = {"user_id": faker.random_number(digits=2), "user_name": faker.word()}

    response = find_user_router.route(HttpRequest(query=attributes))

    # Testing input
    assert find_user_use_case.by_id_and_user_param["user_id"] == attributes["user_id"]
    assert find_user_use_case.by_id_and_user_param["name"] == attributes["user_name"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_by_id():
    """ Testing route method in FindUserRouter """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_router = FindUserRouter(find_user_use_case)
    attributes = {"user_id": faker.random_number(digits=2)}

    response = find_user_router.route(HttpRequest(query=attributes))

    # Testing input
    assert find_user_use_case.by_id_param["user_id"] == attributes["user_id"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_by_name():
    """ Testing route method in FindUserRouter """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_router = FindUserRouter(find_user_use_case)
    attributes = {"user_name": faker.word()}

    response = find_user_router.route(HttpRequest(query=attributes))

    # Testing input
    assert find_user_use_case.by_name_param["name"] == attributes["user_name"]

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_error_no_query():
    """ Testing route method in FindUserRouter """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_router = FindUserRouter(find_user_use_case)

    response = find_user_router.route(HttpRequest())

    # Testing input
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}
    assert find_user_use_case.by_id_and_user_param == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_query():
    """ Testing route method in FindUserRouter """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_router = FindUserRouter(find_user_use_case)

    response = find_user_router.route(HttpRequest(query={"something": faker.word()}))

    # Testing input
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}
    assert find_user_use_case.by_id_and_user_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
