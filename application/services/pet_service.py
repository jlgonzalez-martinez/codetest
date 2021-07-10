""" Pet service module """
import logging
from typing import List, Optional

from application.domain.pet import Pet
from infrastructure.providers.provider import Provider
from utils.singleton_meta import Singleton

LOGGER = logging.getLogger(__name__)


class PetService(metaclass=Singleton):
    """ Pet service class """
    def __init__(self, providers: List[Provider] = None):
        self._providers = providers

    def get_by_provider_and_id(self, pet_id: int, provider_name: str) -> Pet:
        """
        Get a pet identified by a provider name and an id
        Args:
            pet_id: Pet identifier
            provider_name: Provider name

        Returns: Resulting pet
        """
        LOGGER.info(f'Getting pet with id {pet_id} and provider {provider_name}')
        provider = self._get_provider_by_name(provider_name)
        if provider:
            return provider.get_by_id(pet_id)
        else:
            raise ValueError(f'Pet not found with criteria pet_id {pet_id} and provider {provider_name}')

    def get_all(self) -> List[Pet]:
        """
        Get all the pets for all the providers that the api includes

        Returns: List of pets
        """
        pets = []
        for provider in self._providers:
            pets.extend(provider.list())
        return pets

    def _get_provider_by_name(self, provider_name: str) -> Optional[Provider]:
        """
        Get a provider by name from the providers attribute.
        Args:
            provider_name: Provider name

        Returns: Provider by name or None if any provider match with the name

        """
        if self._providers:
            return next(filter(lambda provider: provider.name == provider_name, self._providers), None)
