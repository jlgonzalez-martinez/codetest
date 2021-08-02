""" Test pet service module """
from unittest import TestCase
from unittest.mock import MagicMock

from application.services.pet_service import PetService


class TestPetService(TestCase):
    """ Pet service test class """
    TEST_PET_ID = 1
    PROVIDER_NAME = 'name'

    @classmethod
    def setUpClass(cls):
        """ Set test pet service class """
        cls.pet_service = PetService()

    def test_get_by_provider_and_id_without_any_provider(self):
        """ Test get by provider and id without any provider raises a ValueError """
        self.pet_service._providers = []
        with self.assertRaises(ValueError):
            self.pet_service.get_by_provider_and_id(self.TEST_PET_ID, self.PROVIDER_NAME)

    def test_get_by_provider_and_id_with_a_provider_that_match_the_name(self):
        """ Test get by provider and id with a provider with that name """
        provider_mock = MagicMock()
        provider_mock.name = self.PROVIDER_NAME
        self.pet_service._providers = [provider_mock]
        self.pet_service.get_by_provider_and_id(self.TEST_PET_ID, self.PROVIDER_NAME)
        provider_mock.get_by_id.assert_called_with(self.TEST_PET_ID)

    def test_get_all(self):
        """ Test get all pets calling all the providers """
        provider_mock_1 = MagicMock()
        provider_1 = ['pet_1', 'pet_2']
        provider_mock_1.list.return_value = provider_1
        provider_mock_2 = MagicMock()
        provider_2 = ['pet_3', 'pet_4']
        provider_mock_2.list.return_value = provider_2
        self.pet_service._providers = [provider_mock_1, provider_mock_2]

        pets = self.pet_service.get_all()

        self.assertTrue(provider_mock_1.list.called)
        self.assertTrue(provider_mock_2.list.called)
        self.assertListEqual(provider_1 + provider_2, pets)
