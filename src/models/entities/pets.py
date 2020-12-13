import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src.models.configs import Base


class AnimalTypes(enum.Enum):
    """ Defining Animals Types """

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"

    def __repr__(self):
        return f"Types: [{self.dog}, {self.cat}, {self.fish}, {self.turtle}]"


class Pets(Base):
    """ Pets Entity """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    specie = Column(Enum(AnimalTypes))
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [{self.name}, {self.specie}, {self.age}]"
