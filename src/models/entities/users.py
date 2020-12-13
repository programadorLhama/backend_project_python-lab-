from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.configs import Base


class Users(Base):
    """ Users Entity """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    id_pet = relationship("Pets")

    def __repr__(self):
        return f"User [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.password == other.password
        ):
            return True
        return False
