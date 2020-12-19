from collections import namedtuple
from faker import Faker
from src.models.entities import Pets

faker = Faker()


def mock_pet() -> Pets:
    """Mocking Pet
    :param - None
    :return - Fake Pet registry
    """

    InsertData = namedtuple("Pets", "id name specie age user_id")
    return InsertData(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie="dog",
        age=faker.random_number(digits=1),
        user_id=faker.random_number(digits=5),
    )
