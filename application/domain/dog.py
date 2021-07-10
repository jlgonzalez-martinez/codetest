""" Dog class module """
from dataclasses import dataclass

from .pet import Pet


@dataclass
class Dog(Pet):
    """ Dog class """

    @classmethod
    def from_dict(cls, pet_dict: dict):
        """
        Get a Dog from a dict discarding extra fields

        Args:
            - pet_dict: Dog dictionary

        Returns:
            Result pet created from dict

        """
        return cls(id=pet_dict['id'], provider=pet_dict['provider'], name=pet_dict['name'],
                   weight=pet_dict['weight'], height=pet_dict['height'], length=pet_dict['length'],
                   description=pet_dict['description'], photo_url=pet_dict['photo_url'])
