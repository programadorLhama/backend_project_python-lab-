# pylint: disable=E1101

from collections import namedtuple
from typing import List
from src.models.entities import Users
from src.models.configs import DBConnectionHandler
from src.data.interfaces import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """ Class to manage User Repository """

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
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

                return InsertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
        Select data in user entity by id and/or name
        :param  - id: Id of the registry
                - name: User name in database
        :return - List with users selected
        """

        try:
            query_data = None

            if user_id and not name:
                # Select user by id
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(Users).filter_by(id=user_id).one()
                    )
                    query_data = [data]

            elif not user_id and name:
                # Select user by name
                with DBConnectionHandler() as db_connection:
                    query_data = (
                        db_connection.session.query(Users).filter_by(name=name).all()
                    )

            elif user_id and name:
                # Select user by id and name
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(Users)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
