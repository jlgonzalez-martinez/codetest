""" HTTP provider module """
import logging
from http import HTTPStatus
from typing import List

import requests
from cachetools import cached, TTLCache

from application.converters.converter import Converter
from application.domain.pet import Pet
from application.mappers.mapper import Mapper
from .provider import Provider

LOGGER = logging.getLogger(__name__)


class HttpProvider(Provider):
    """ Http provider class """

    def __init__(self, name: str, protocol: str, host: str, port: int, routes: List[str],
                 converters: List[Converter] = None, mapper: Mapper = None):
        super().__init__(name, converters=converters, mapper=mapper)
        self._url = f'{protocol}://{host}:{port}'
        self._routes = routes

    def list(self) -> List[Pet]:
        """
        Return all the pets for the current provider adding the results from all routes

        Returns: List of all pets present in the current provider

        """
        pets = []
        for route in self._routes:
            LOGGER.info(f'Get all pets from provider {self.name} in route {route}')
            response = self.execute_request(f'{self._url}{route}')
            if response.status_code == HTTPStatus.OK:
                pets.extend([self._convert_pet(self._map_pet(pet, route=route)) for pet in response.json()])
        return pets

    def get_by_id(self, pet_id: int) -> Pet:
        """
        Get a pet by id searching in all the defining routes

        Args:
            - pet_id: Pet identifier

        Returns: Pet identified by it's id

        """
        for route in self._routes:
            LOGGER.info(f'Try to get pet with id {pet_id} from provider {self.name} in route {route}')
            response = self.execute_request(f'{self._url}{route}{pet_id}')
            if response.status_code == HTTPStatus.OK and response.json():
                return self._convert_pet(self._map_pet(response.json(), route=route))

    @staticmethod
    @cached(TTLCache(ttl=600, maxsize=500))
    def execute_request(url: str):
        """
        Execute request to a third party

        Args:
            url: Input url

        Returns: HTTP Response

        """
        return requests.get(url)
