""" Provider factory test module """
from unittest import TestCase
from unittest.mock import patch

from infrastructure.providers.http_provider import HttpProvider
from infrastructure.providers.provider_factory import provider_factory


@patch('infrastructure.providers.provider_factory.converter_factory')
@patch('infrastructure.providers.provider_factory.mapper_factory')
class TestProviderFactory(TestCase):
    """ Provider factory test class """
    TEST_NAME = 'name'
    TEST_PROTOCOL = 'http'
    TEST_HOST = 'host'
    TEST_PORT = 'port'
    TEST_ROUTES = ['route_1', 'route_2']
    TEST_MAPPER = 'mapper'
    TEST_CONVERTER = 'converter'

    def test_http_provider_factory(self, mapper_factory_mock, converter_factory_mock):
        """ Test provider factory with a http provider """
        http_provider_settings = dict(http_provider=dict(name=self.TEST_NAME,
                                                         protocol=self.TEST_PROTOCOL,
                                                         host=self.TEST_HOST,
                                                         port=self.TEST_PORT,
                                                         routes=self.TEST_ROUTES,
                                                         mapper=self.TEST_MAPPER,
                                                         converters=[self.TEST_CONVERTER]))
        http_provider = provider_factory(http_provider_settings)
        mapper_factory_mock.assert_called_with(self.TEST_MAPPER)
        converter_factory_mock.assert_called_with(self.TEST_CONVERTER)
        self.assertIsInstance(http_provider, HttpProvider)
        self.assertEqual(self.TEST_NAME, http_provider.name)
        self.assertListEqual(self.TEST_ROUTES, http_provider._routes)
        self.assertEqual(f'{self.TEST_PROTOCOL}://{self.TEST_HOST}:{self.TEST_PORT}', http_provider._url)

    def test_http_provider_factory_without_converters(self, mapper_factory_mock, converter_factory_mock):
        """ Test provider factory with a http provider """
        http_provider_settings = dict(http_provider=dict(name=self.TEST_NAME,
                                                         protocol=self.TEST_PROTOCOL,
                                                         host=self.TEST_HOST,
                                                         port=self.TEST_PORT,
                                                         routes=self.TEST_ROUTES,
                                                         mapper=self.TEST_MAPPER))
        http_provider = provider_factory(http_provider_settings)
        mapper_factory_mock.assert_called_with(self.TEST_MAPPER)
        self.assertFalse(converter_factory_mock.called)
        self.assertIsInstance(http_provider, HttpProvider)
        self.assertEqual(self.TEST_NAME, http_provider.name)
        self.assertListEqual(self.TEST_ROUTES, http_provider._routes)
        self.assertEqual(f'{self.TEST_PROTOCOL}://{self.TEST_HOST}:{self.TEST_PORT}', http_provider._url)

    def test_provider_factory_with_an_incorrect_provider_name(self, _, __):
        """ Tests that the provider factory raises an error with an incorrect name """
        test_settings = dict(test='test')
        with self.assertRaises(NotImplementedError):
            provider_factory(dict(fake_provider=test_settings))

    def test_provider_factory_with_no_mapper(self, _, __):
        """ Tests that the provider factory raises an error with no mappers configured """
        test_settings = dict(name=self.TEST_NAME,
                             protocol=self.TEST_PROTOCOL,
                             host=self.TEST_HOST,
                             port=self.TEST_PORT,
                             routes=self.TEST_ROUTES,
                             converters=[])
        with self.assertRaises(ValueError):
            provider_factory(dict(http_provider=test_settings))
