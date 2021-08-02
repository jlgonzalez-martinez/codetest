""" Http provider test module """
from unittest import TestCase
from unittest.mock import patch, MagicMock

from infrastructure.providers.http_provider import HttpProvider


@patch('infrastructure.providers.http_provider.requests')
class TestHttpProvider(TestCase):
    """ Http provider test class """
    TEST_NAME = 'name'
    TEST_PROTOCOL = 'http'
    TEST_HOST = 'host'
    TEST_PORT = 9090
    TEST_ROUTE_1 = 'route_1'
    TEST_ROUTE_2 = 'route_2'
    TEST_ROUTES = [TEST_ROUTE_1, TEST_ROUTE_2]
    TEST_PET_DICT = dict(name='name')

    def test_list_calls_all_routes_and_join_results(self, requests_mock):
        """ Test http provider list call the urls and merge the results """
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = [self.TEST_PET_DICT]
        requests_mock.get.return_value = response_mock

        converter_mock = MagicMock()
        converter_mock.convert.return_value = self.TEST_PET_DICT

        mapper_mock = MagicMock()
        mapper_mock.map_pet.return_value = self.TEST_PET_DICT

        http_provider = HttpProvider(name=self.TEST_NAME, protocol=self.TEST_PROTOCOL, host=self.TEST_HOST,
                                     port=self.TEST_PORT, routes=self.TEST_ROUTES, converters=[converter_mock],
                                     mapper=mapper_mock)

        pet_list = http_provider.list()

        mapper_mock.map_pet.assert_any_call(self.TEST_PET_DICT, route=self.TEST_ROUTE_1)
        mapper_mock.map_pet.assert_any_call(self.TEST_PET_DICT, route=self.TEST_ROUTE_2)
        converter_mock.convert.assert_any_call(self.TEST_PET_DICT)
        self.assertEqual(2, converter_mock.convert.call_count)
        self.assertListEqual([self.TEST_PET_DICT, self.TEST_PET_DICT], pet_list)

    def test_get_by_id_calls_all_routes_and_join_results(self, requests_mock):
        """ Test http provider get_by id call the urls and return the first result """
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = self.TEST_PET_DICT
        requests_mock.get.return_value = response_mock

        converter_mock = MagicMock()
        converter_mock.convert.return_value = self.TEST_PET_DICT

        mapper_mock = MagicMock()
        mapper_mock.map_pet.return_value = self.TEST_PET_DICT

        http_provider = HttpProvider(name=self.TEST_NAME, protocol=self.TEST_PROTOCOL, host=self.TEST_HOST,
                                     port=self.TEST_PORT, routes=self.TEST_ROUTES, converters=[converter_mock],
                                     mapper=mapper_mock)

        pet = http_provider.get_by_id(0)

        mapper_mock.map_pet.assert_called_once_with(self.TEST_PET_DICT, route=self.TEST_ROUTE_1)
        converter_mock.convert.assert_called_once_with(self.TEST_PET_DICT)
        self.assertEqual(self.TEST_PET_DICT, pet)
