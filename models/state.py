from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State class"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage: Represents a relationship with the class City
    # If the State object is deleted, all linked City objects must be automatically deleted
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    # For FileStorage: Getter attribute cities that returns the list of City instances
    # with state_id equals to the current State.id
    @property
    def cities(self):
        """Getter attribute to return the list of City instances"""
        from models import storage
        from models.city import City
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list