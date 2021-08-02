""" Mappers module """
from .converter import Converter
from ..domain.pet import Pet


class WeightConverter(Converter):
    """ Field mapper class """
    FIELDS = ['weight']

    def convert(self, pet: Pet) -> Pet:
        """
        Convert grams to kilograms for the weight fields
        Args:
            pet: Input pet

        Returns: Converted pet

        """
        for field in self.FIELDS:
            pet.__setattr__(field, self._convert_from_grams_to_kilo_grams(pet.__getattribute__(field)))
        return pet

    @staticmethod
    def _convert_from_grams_to_kilo_grams(input_weight: float) -> float:
        """
        Convert input weight from grams to kilo grams
        Args:
            input_weight: Input pet weight

        Returns: Result weight

        """
        return input_weight / 1000
