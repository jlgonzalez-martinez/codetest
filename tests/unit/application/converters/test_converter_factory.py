""" Converter factory test module """
from unittest import TestCase

from application.converters.converter_factory import converter_factory
from application.converters.weight_converter import WeightConverter


class TestConverterFactory(TestCase):
    """ Converter factory test class """

    def test_weight_converter_factory(self):
        """ Test converter factory with a weight converter """
        weight_converter = converter_factory('weight_converter')
        self.assertIsInstance(weight_converter, WeightConverter)

    def test_converter_factory_with_an_incorrect_provider_name(self):
        """ Tests that the mapper factory raises an error with an incorrect name """
        with self.assertRaises(NotImplementedError):
            converter_factory('fake_converter')
