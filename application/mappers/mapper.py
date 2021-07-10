""" Mappers module """
from abc import abstractmethod
from typing import Dict


class Mapper:
    """ Base mapper class """

    def __init__(self, rename_fields: Dict[str, str] = None):
        self._rename_fields = rename_fields if rename_fields else dict()

    @abstractmethod
    def map_pet(self, pet_dict: dict, route: str = None):
        """ Map a pet dictionary to a domain pet object """
        raise NotImplementedError

    def normalize(self, pet_dict: dict) -> dict:
        """
        Remap pet dict using the rename fields attributes.
        This allows us to map different attributes names between the apis.

        Args:
            pet_dict: Input pet dictionary

        Returns: Modified pet dictionary
        """
        for key, value in self._rename_fields.items():
            if key in pet_dict:
                pet_dict[value] = pet_dict.pop(key)
        return pet_dict
