""" Mappers module """
from .mapper import Mapper
from ..domain.pet_type import PetType


class RouteMapper(Mapper):
    """ Field mapper class """

    def map_pet(self, pet_dict: dict, route: str = None):
        """
        Map a pet dictionary to a domain pet object
        Args:
            pet_dict: Pet info dictionary
            route: Pet route

        Returns: Mapped pet
        """
        normalize_pet_dict = self.normalize(pet_dict)
        pet_class = PetType.from_pet_name(route).pet_class
        return pet_class.from_dict(normalize_pet_dict)
