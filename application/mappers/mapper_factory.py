""" Provider factory module"""
from typing import Dict, Union, Optional, Any

from .field_mapper import FieldMapper
from .route_mapper import RouteMapper
from .mapper import Mapper

from enum import Enum


class MapperType(Enum):
    """
    Mapper type enumeration:
    - FIELD_MAPPER: Field mapper
    - ROUTE_MAPPER: Route mapper
    """
    FIELD_MAPPER = ('field_mapper', FieldMapper)
    ROUTE_MAPPER = ('route_mapper', RouteMapper)

    @property
    def mapper_name(self) -> str:
        """
        Mapper enum name

        Returns: Mapper config name

        """
        return self.value[0]

    @property
    def interface(self) -> Mapper:
        """
        Mapper interface

        Returns: current provider interface

        """
        return self.value[1]

    @staticmethod
    def from_mapper_name(mapper_name: str):
        """
        Get the enum value for the specified mapper name

        Args:
            mapper_name: mapper name to get the mapper type

        Returns: enumeration value for the configured mapper type

        """
        return next(filter(lambda member: member.mapper_name == mapper_name, MapperType), None)


def mapper_factory(mapper_settings:Dict[str, Any]) -> Mapper:
    """
    Provider interface factory

    Args:
        mapper_settings: application settings

    Returns: communications interface for the configured shared storage with the provided settings

    """
    mapper_name = mapper_settings.pop('name')
    return _get_mapper(mapper_name, mapper_settings)


def _get_mapper(mapper_name: str, mapper_settings: Optional[dict] = None):
    """
    Get a mapper for a specific mapper name and settings
    Args:
        mapper_name: Mapper name
        mapper_settings: Mapper settings

    Returns: Result mapper
    """
    mapper_type = MapperType.from_mapper_name(mapper_name)
    if mapper_type:
        if mapper_settings:
            mapper = mapper_type.interface(**mapper_settings)
        else:
            mapper = mapper_type.interface()
        return mapper
    else:
        raise NotImplementedError(f'Mapper of type {mapper_name} is not implemented')
