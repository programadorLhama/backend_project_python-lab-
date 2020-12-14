# pylint: disable=E1101

from collections import namedtuple
from typing import Tuple
from src.models.entities import Pets
from src.models.configs import DBConnectionHandler


class PetRepository:
    """ Class to manage Pet Repository """

    @classmethod
    def insert_pet(
        cls, name: str, specie: str, age: int, user_id: int
    ) -> Tuple[int, str, str, int, int]:
        """
        Insert data in pets entity
        :param  - name: person name
                - specie: Enum with species acepted
                - age: age of the pet
                - user_id: id of the owner (FK)
        :return - tuple with new pet inserted informations
        """

        InsertData = namedtuple("Pets", "id name specie age user_id")

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = Pets(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return InsertData(
                    id=new_pet.id, name=name, specie=specie, age=age, user_id=user_id
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
