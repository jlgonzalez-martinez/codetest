""" Converter factory test module """
from unittest import TestCase

from application.converters.weight_converter import WeightConverter
from application.domain.dog import Dog


class TestWeightConverter(TestCase):
    """ Converter factory test class """

    def test_convert(self):
        """ Test convert changes from grams to kilo grams """
        weight_converter = WeightConverter()
        test_dog = Dog(id=1, provider='test_provider', name='name',
                       weight=1500, height=1, length=1, description='', photo_url='')
        convert_dog = weight_converter.convert(test_dog)
        self.assertEqual(1.5, convert_dog.weight)
