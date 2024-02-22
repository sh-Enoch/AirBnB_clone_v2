#!/usr/bin/python3

from sqlalchemy import Column, String
# from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, storage_type


class State(BaseModel, Base):
    """ State class """
    # from models.city import City

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with state_id equals
               to the current State.id"""
            from models.city import City
            from models import storage
            city_instances = storage.all(City)
            return [city for city in city_instances.values() if city.state_id == self.id]
