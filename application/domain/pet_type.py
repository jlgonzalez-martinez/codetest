""" Pet type module """
from enum import Enum

from application.domain.cat import Cat
from application.domain.dog import Dog
from application.domain.pet import Pet


class PetType(Enum):
    """
    Shared storage type enumeration:
    - HTTP_PROVIDER: Http provider
    """
    CAT = ('cat', Cat)
    DOG = ('dog', Dog)

    @property
    def provider_name(self) -> str:
        """
        Pet class name

        Returns: Mapper description name

        """
        return self.value[0]

    @property
    def pet_class(self) -> Pet:
        """
        Pet class

        Returns: current provider interface

        """
        return self.value[1]

    @staticmethod
    def from_pet_name(pet_name: str):
        """
        Get the enum value that contains specified provider name

        Args:
            pet_name: provider name to get the pet type

        Returns: enumeration value for the pet name

        """
        return next(filter(lambda member: member.provider_name in pet_name, PetType), None)

