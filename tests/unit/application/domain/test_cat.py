""" Test cat module """
from unittest import TestCase

from application.domain.cat import Cat


class TestCat(TestCase):
    """ Test cat class """
    TEST_ID = 0
    TEST_PROVIDER = 'prov'
    TEST_NAME = 'name'
    TEST_WEIGHT = 1
    TEST_HEIGHT = 1
    TEST_LENGTH = 1
    TEST_DESCRIPTION = 'desc'
    TEST_PHOTO = 'photo'
    TEST_NUMBER_OF_LIVES = 9

    def test_from_dict(self):
        """ Tests cats from dict """
        cat_dict = dict(id=self.TEST_ID, provider=self.TEST_PROVIDER, name=self.TEST_NAME, weight=self.TEST_WEIGHT,
                        height=self.TEST_HEIGHT, length=self.TEST_LENGTH, description=self.TEST_DESCRIPTION,
                        photo_url=self.TEST_PHOTO, number_of_lives=self.TEST_NUMBER_OF_LIVES)
        cat = Cat.from_dict(cat_dict)
        self.assertIsInstance(cat, Cat)
        self.assertEqual(self.TEST_ID, cat.id)
        self.assertEqual(self.TEST_NUMBER_OF_LIVES, cat.number_of_lives)
