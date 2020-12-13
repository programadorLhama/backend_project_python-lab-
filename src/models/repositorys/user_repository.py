# pylint: disable=E1101

from collections import namedtuple
from src.models.entities import Users
from src.models.configs import DBConnectionHandler


class UserRepository:
    """ Class to manage User Repository """

    @classmethod
    def insert_user(cls, name: str, password: str) -> tuple:
        """
        Insert data in user entity
        :param  - name: person name
                - password: user password
        :return - tuple with new user inserted informations
        """

        # Creating a Return Tuple With Informations
        InsertData = namedtuple("Users", "id name password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return InsertData(id=new_user.id, name=new_user.name, password=password)

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
