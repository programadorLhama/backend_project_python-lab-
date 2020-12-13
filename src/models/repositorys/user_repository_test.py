from faker import Faker
from src.models.configs import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
db_connection_handler = DBConnectionHandler()
user_repository = UserRepository()


def test_insert_user():
    """ Should insert user in Users table and get it """

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    # SQL commands
    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password

    engine.execute("DELETE FROM users WHERE id='{}';".format(new_user.id))
