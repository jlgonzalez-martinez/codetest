""" Mappers module """
from typing import Dict

from .mapper import Mapper
from ..domain.pet_type import PetType


class FieldMapper(Mapper):
    """ Field mapper class """

    def __init__(self, field_name, rename_fields: Dict[str, str] = None):
        super().__init__(rename_fields=rename_fields)
        self._field_name = field_name

    def map_pet(self, pet_dict: dict, route: str = None):
        """
        Map a pet dictionary to a domain pet object
        Args:
            pet_dict: Pet info dictionary
            route: Pet route

        Returns: Mapped pet

        """
        normalize_pet_dict = self.normalize(pet_dict)
        if self._field_name in normalize_pet_dict:
            kind_field = pet_dict.pop(self._field_name)
            pet_class = PetType.from_pet_name(kind_field).pet_class
            return pet_class.from_dict(normalize_pet_dict)
