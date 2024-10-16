import logging
import sys
from unittest import TestCase, skip
from unittest.mock import patch

import boto3
from botocore.stub import Stubber
from mockito import when

from libumccr import aws

logger = logging.getLogger(__name__)


class LibSmUnitTests(TestCase):

    def setUp(self):
        from libumccr.aws import libsm
        mock_sm_client = boto3.client('secretsmanager')
        stubber = Stubber(mock_sm_client)
        stubber.add_response('get_secret_value', {
            'SecretString': 'HealTheWorld',  # pragma: allowlist secret
        })
        stubber.activate()
        when(aws).sm_client(...).thenReturn(mock_sm_client)
        when(libsm).sm_client(...).thenReturn(mock_sm_client)

    def test_cache_clear(self):
        """
        python -m unittest tests.aws.test_libsm.LibSmUnitTests.test_cache_clear
        """
        from libumccr.aws import libsm
        # logger.info(dir(libsm.get_secret))
        # logger.info(type(libsm.get_secret))
        libsm.get_secret.cache_clear()
        self.assertTrue(hasattr(libsm.get_secret, "cache_clear"))

    @patch.dict(sys.modules, {"cachetools": None})
    @patch("libumccr.utils.load_package_if_found")
    def test_cache_clear_cachetools_not_found(self, load_package_if_found):
        """
        python -m unittest tests.aws.test_libsm.LibSmUnitTests.test_cache_clear_cachetools_not_found
        """
        load_package_if_found.return_value = False

        from libumccr.aws import libsm
        libsm.get_secret.cache_clear()

        self.assertIsNone(sys.modules['cachetools'])
        self.assertTrue(hasattr(libsm.get_secret, "cache_clear"))

    @patch.dict(sys.modules, {"cachetools": None})
    @patch("libumccr.utils.load_package_if_found")
    def test_get_secret_no_cache(self, load_package_if_found):
        """
        python -m unittest tests.aws.test_libsm.LibSmUnitTests.test_get_secret_no_cache
        """
        load_package_if_found.return_value = False

        from libumccr.aws import libsm
        libsm.get_secret.cache_clear()
        value = libsm.get_secret(secret_name='MyTestSecret')
        logger.info(value)
        self.assertEqual(value, 'HealTheWorld')
        self.assertIsNone(sys.modules['cachetools'])

    def test_get_secret(self):
        """
        python -m unittest tests.aws.test_libsm.LibSmUnitTests.test_get_secret
        """

        from libumccr.aws import libsm
        value = libsm.get_secret(secret_name='MyTestSecret')
        logger.info(value)
        self.assertEqual(value, 'HealTheWorld')


class LibSmIntegrationTests(TestCase):

    @skip
    def test_get_secret(self):
        """
        python -m unittest tests.aws.test_libsm.LibSmIntegrationTests.test_get_secret
        """
        from libumccr.aws import libsm
        lookup_name = "IcaSecretsPortal"

        secret = libsm.get_secret(secret_name=lookup_name)

        self.assertIsNotNone(secret)
        self.assertIsInstance(secret, str)
        logger.info(secret)
