""" Abstract provider module """
from abc import abstractmethod
from typing import List, Callable

from application.converters.converter import Converter
from application.domain.pet import Pet
from application.mappers.mapper import Mapper


class Provider:
    """ Provider class """

    def __init__(self, name: str, converters: List[Converter] = None, mapper: Mapper = None):
        self._name = name
        self._mapper = mapper
        self._converters = converters if converters else []

    @property
    def name(self):
        """
        Name property

        Returns: Name of the provider
        """
        return self._name

    @property
    def mapper(self) -> Mapper:
        """
        Mapper property

        Returns: Mapper of the provider
        """
        return self._mapper

    @property
    def converters(self) -> List[Converter]:
        """
        Mapper property

        Returns: Mapper of the provider
        """
        return self._converters

    @abstractmethod
    def list(self) -> List[Pet]:
        """
        List method, should return the list of pets, for the specific client

        Returns:
            List of pets of the specific client

        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, pet_id: int) -> Pet:
        """
        Get by id method, should return a pet specifying it's id in the specific provider

        Args:
            - pet_id: Pet identifier

        Returns: Pet with the specified id

        """
        raise NotImplementedError

    def _map_pet(self, pet_dict: dict, route: str = None):
        """
        Map pet using the configured mapper
        Args:
            pet_dict: Pet dictionary
            route: Input route

        Returns: Mapped pet
        """
        pet_dict['provider'] = self._name
        return self.mapper.map_pet(pet_dict, route=route)

    def _convert_pet(self, pet: Pet) -> Pet:
        """
        Convert a pet instance executing all the converters configured

        Args:
            pet: Input pet

        Returns: The converted pet

        """
        for conv in self.converters:
            pet = conv.convert(pet)
        return pet
