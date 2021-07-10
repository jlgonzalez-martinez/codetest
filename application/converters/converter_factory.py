""" Provider factory module"""
from typing import Dict, Union, Optional, Any


from .converter import Converter
from .weight_converter import WeightConverter

from enum import Enum


class ConverterType(Enum):
    """
    Mapper type enumeration:
    - WEIGHT_MAPPER: Weight mapper
    """
    WEIGHT_CONVERTER = ('weight_converter', WeightConverter)

    @property
    def converter_name(self) -> str:
        """
        Converter enum name

        Returns: Converter config name

        """
        return self.value[0]

    @property
    def interface(self) -> Converter:
        """
        Converter interface

        Returns: current converter interface

        """
        return self.value[1]

    @staticmethod
    def from_converter_name(converter_name: str):
        """
        Get the enum value for the specified converter name

        Args:
            converter_name: mapper name to get the mapper type

        Returns: enumeration value for the configured converter type

        """
        return next(filter(lambda member: member.converter_name == converter_name, ConverterType), None)


def converter_factory(converter_name: str) -> Converter:
    """
    Converter interface factory

    Args:
        converter_name: Converter name

    Returns: converter interface for the input converter name

    """
    converter_type = ConverterType.from_converter_name(converter_name)
    if converter_type:
        return converter_type.interface()
    else:
        raise NotImplementedError(f'Converter of type {converter_name} is not implemented')
