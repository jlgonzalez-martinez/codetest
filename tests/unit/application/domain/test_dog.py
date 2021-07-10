""" Test dog module """
from unittest import TestCase

from application.domain.dog import Dog


class TestDog(TestCase):
    """ Test dog class """
    TEST_ID = 0
    TEST_PROVIDER = 'prov'
    TEST_NAME = 'name'
    TEST_WEIGHT = 1
    TEST_HEIGHT = 1
    TEST_LENGTH = 1
    TEST_DESCRIPTION = 'desc'
    TEST_PHOTO = 'photo'

    def test_from_dict(self):
        """ Tests dogs from dict """
        dog_dict = dict(id=self.TEST_ID, provider=self.TEST_PROVIDER, name=self.TEST_NAME, weight=self.TEST_WEIGHT,
                        height=self.TEST_HEIGHT, length=self.TEST_LENGTH, description=self.TEST_DESCRIPTION,
                        photo_url=self.TEST_PHOTO)
        dog = Dog.from_dict(dog_dict)
        self.assertIsInstance(dog, Dog)
        self.assertEqual(self.TEST_ID, dog.id)
