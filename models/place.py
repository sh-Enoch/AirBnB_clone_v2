from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, storage_type
from models.city import Amenity

class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if storage_type == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                             Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                             Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances based on amenity_ids"""
            from models import storage
            amenity_instances = storage.all(Amenity)
            return [amenity for amenity in amenity_instances.values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute that handles appending Amenity.id to amenity_ids"""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
            else:
                pass
