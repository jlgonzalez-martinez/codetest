""" Pet class module """
from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Pet:
    """ Animal base class that define all the attributes for an animal """
    id: int
    provider: str
    name: str
    weight: float
    height: int
    length: int
    description: str
    photo_url: str
    kind: Optional[str] = None

    @classmethod
    @abstractmethod
    def from_dict(cls, pet_dict: dict):
        """
        Get the dataclass from a dict discarding extra fields

        Args:
            - pet_dict: Pet dictionary

        Returns:
            Result pet created from dict

        """
        raise NotImplementedError
