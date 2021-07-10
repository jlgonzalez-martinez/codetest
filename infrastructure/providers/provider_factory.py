""" Provider factory module"""
from typing import Dict

from application.converters.converter_factory import converter_factory
from application.mappers.mapper_factory import mapper_factory
from .http_provider import HttpProvider
from .provider import Provider

from enum import Enum


class ProviderType(Enum):
    """
    Shared storage type enumeration:
    - HTTP_PROVIDER: Http provider
    """
    HTTP_PROVIDER = ('http_provider', HttpProvider)

    @property
    def provider_name(self) -> str:
        """
        Provider enum name

        Returns: Provider config name

        """
        return self.value[0]

    @property
    def interface(self) -> Provider:
        """
        Provider interface

        Returns: current provider interface

        """
        return self.value[1]

    @staticmethod
    def from_provider_name(provider_name: str):
        """
        Get the enum value for the specified provider name

        Args:
            provider_name: provider name to get the provider type

        Returns: enumeration value for the configured provider type

        """
        return next(filter(lambda member: member.provider_name == provider_name, ProviderType), None)


def provider_factory(settings: Dict[str, dict]) -> Provider:
    """
    Provider interface factory

    Args:
        settings: application settings

    Returns: provider interface for the configured provided

    """
    provider_name = list(settings.keys())[0]
    provider_conf = settings[provider_name]
    provider_type = ProviderType.from_provider_name(provider_name)
    if provider_type:
        _configure_mapper(provider_conf)
        _configure_converters(provider_conf)
        return provider_type.interface(**provider_conf)
    else:
        raise NotImplementedError(f'Provider of type {provider_name} is not implemented')


def _configure_mapper(provider_conf: dict):
    """
    Map the provider conf mapper using the mapper factory

    Args:
        provider_conf: Provided configuration

    """
    if 'mapper' in provider_conf:
        mapper_conf = provider_conf['mapper']
        provider_conf['mapper'] = mapper_factory(mapper_conf)
    else:
        raise ValueError('At least one mapper have to be configured')


def _configure_converters(provider_conf: dict):
    """
    Map the provider conf converters using the converter factory

    Args:
        provider_conf: Provided configuration

    """
    if 'converters' in provider_conf:
        provider_conf['converters'] = [converter_factory(conv) for conv in provider_conf['converters']]
