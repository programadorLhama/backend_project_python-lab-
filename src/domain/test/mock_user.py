from collections import namedtuple
from faker import Faker
from src.infra.entities import Users

faker = Faker()


def mock_users() -> Users:
    """Mocking Users
    :param - None
    :param Fake User registry
    """

    InsertData = namedtuple("Users", "id name password")
    return InsertData(
        id=faker.random_number(digits=5), name=faker.name(), password=faker.name()
    )
