""" Converter module """
from abc import abstractmethod

from application.domain.pet import Pet


class Converter:
    """ Base converter class """
    FIELDS = []

    @abstractmethod
    def convert(self, pet: Pet) -> Pet:
        """ Convert a pet modifying it's attributes"""
        raise NotImplementedError
