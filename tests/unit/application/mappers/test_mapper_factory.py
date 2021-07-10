""" Mapper factory test module """
from unittest import TestCase

from application.mappers.field_mapper import FieldMapper
from application.mappers.route_mapper import RouteMapper
from application.mappers.mapper_factory import mapper_factory


class TestMapperFactory(TestCase):
    """ Mapper factory test class """
    TEST_FIELD_NAME = 'field'

    def test_route_mapper_factory(self):
        """ Test mapper factory with a route mapper """
        rename_fields = dict(picture='photo_url')
        route_mapper = mapper_factory(dict(name='route_mapper', rename_fields=rename_fields))
        self.assertIsInstance(route_mapper, RouteMapper)
        self.assertDictEqual(rename_fields, route_mapper._rename_fields)

    def test_field_mapper_factory(self):
        """ Test mapper factory with a field mapper """
        field_mapper = mapper_factory(dict(name='field_mapper', field_name=self.TEST_FIELD_NAME))
        self.assertIsInstance(field_mapper, FieldMapper)
        self.assertEqual(self.TEST_FIELD_NAME, field_mapper._field_name)

    def test_provider_factory_with_an_incorrect_provider_name(self):
        """ Tests that the mapper factory raises an error with an incorrect name """
        with self.assertRaises(NotImplementedError):
            mapper_factory(dict(name='fake_provider'))
