""" Route mapper test module """
from unittest import TestCase

from application.domain.dog import Dog
from application.mappers.route_mapper import RouteMapper


class TestRouteMapper(TestCase):
    """ Mapper factory test class """
    TEST_DOG_ROUTE = '/test/dogs/'

    def test_route_mapper_without_renaming_fields(self):
        """ Tests route mapper with a dog that not needs to rename fields """
        input_dog = dict(id=1, provider='test_provider', name='name',
                         weight=1500, height=1, length=1, description='', photo_url='')
        mapper = RouteMapper()
        dog = mapper.map_pet(input_dog, route=self.TEST_DOG_ROUTE)

        self.assertIsInstance(dog, Dog)
        self.assertEqual(input_dog['name'], dog.name)

    def test_route_mapper_renaming_fields(self):
        """ Tests route mapper with a dog that needs to rename fields """
        test_picture = 'picture'
        input_dog = dict(id=1, provider='test_provider', name='name',
                         weight=1500, height=1, length=1, description='', picture=test_picture)
        mapper = RouteMapper(rename_fields=dict(picture='photo_url'))
        dog = mapper.map_pet(input_dog, route=self.TEST_DOG_ROUTE)

        self.assertIsInstance(dog, Dog)
        self.assertEqual(input_dog['name'], dog.name)
        self.assertEqual(test_picture, dog.photo_url)

