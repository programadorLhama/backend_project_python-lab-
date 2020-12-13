from faker import Faker
from src.models.entities import Users
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


def test_select_user():
    """ Should select a user in Users table compare it """

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = Users(id=user_id, name=name, password=password)
    engine = db_connection_handler.get_engine()

    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}','{}', '{}');".format(
            user_id, name, password
        )
    )
    query_users1 = user_repository.select_user(user_id=user_id)
    query_users2 = user_repository.select_user(name=name)
    query_users3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_users1
    assert data in query_users2
    assert data in query_users3

    engine.execute("DELETE FROM users WHERE id='{}';".format(user_id))
