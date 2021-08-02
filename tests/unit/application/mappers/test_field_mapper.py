""" Route mapper test module """
from unittest import TestCase

from application.domain.dog import Dog
from application.mappers.field_mapper import FieldMapper


class TestFieldMapper(TestCase):
    """ Mapper factory test class """

    def test_field_mapper_without_renaming_fields(self):
        """ Tests field mapper with a dog that not needs to rename fields """
        input_dog = dict(id=1, provider='test_provider', name='name', kind='dog',
                         weight=1500, height=1, length=1, description='', photo_url='')
        mapper = FieldMapper(field_name='kind')
        dog = mapper.map_pet(input_dog)

        self.assertIsInstance(dog, Dog)
        self.assertEqual(input_dog['name'], dog.name)

    def test_field_mapper_without_field_name_in_dict_returns_none(self):
        """ Tests field mapper with a dog dict with no kind provided"""
        input_dog = dict(id=1, provider='test_provider', name='name',
                         weight=1500, height=1, length=1, description='', photo_url='')
        mapper = FieldMapper(field_name='kind')
        dog = mapper.map_pet(input_dog)

        self.assertIsNone(dog)

    def test_route_mapper_renaming_fields(self):
        """ Tests route mapper with a dog that needs to rename fields """
        test_picture = 'picture'
        input_dog = dict(id=1, provider='test_provider', name='name', kind='dog',
                         weight=1500, height=1, length=1, description='', picture=test_picture)
        mapper = FieldMapper(rename_fields=dict(picture='photo_url'), field_name='kind')
        dog = mapper.map_pet(input_dog)

        self.assertIsInstance(dog, Dog)
        self.assertEqual(input_dog['name'], dog.name)
        self.assertEqual(test_picture, dog.photo_url)

