import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src.models.configs import Base


class AnimalTypes(enum.Enum):
    """ Defining Animals Types """

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """ Pets Entity """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    specie = Column(Enum(AnimalTypes))
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, age={self.age}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.user_id == other.user_id
        ):
            return True

        return False
