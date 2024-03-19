import logging
import sys
import uuid
from unittest import TestCase, skip
from unittest.mock import patch

from mockito import when

from libumccr import aws

logger = logging.getLogger(__name__)


class LibSsmUnitTests(TestCase):

    def setUp(self):
        from libumccr.aws import libssm
        mock_ssm = aws.client(
            'ssm',
            endpoint_url='http://localhost:4566',
            region_name='ap-southeast-2',
            aws_access_key_id=str(uuid.uuid4()),
            aws_secret_access_key=str(uuid.uuid4()),
            aws_session_token=f"{uuid.uuid4()}_{uuid.uuid4()}"
        )
        when(aws).ssm_client(...).thenReturn(mock_ssm)
        when(libssm).ssm_client(...).thenReturn(mock_ssm)

    def test_cache_clear(self):
        """
        python -m unittest tests.aws.test_libssm.LibSsmUnitTests.test_cache_clear
        """
        from libumccr.aws import libssm
        # logger.info(dir(libssm.get_secret))
        # logger.info(type(libssm.get_secret))
        libssm.get_secret.cache_clear()
        self.assertTrue(hasattr(libssm.get_secret, "cache_clear"))

    @patch.dict(sys.modules, {"cachetools": None})
    @patch("libumccr.utils.load_package_if_found")
    def test_cache_clear_cachetools_not_found(self, load_package_if_found):
        """
        python -m unittest tests.aws.test_libssm.LibSsmUnitTests.test_cache_clear_cachetools_not_found
        """
        load_package_if_found.return_value = False

        from libumccr.aws import libssm
        libssm.get_secret.cache_clear()

        self.assertIsNone(sys.modules['cachetools'])
        self.assertTrue(hasattr(libssm.get_secret, "cache_clear"))

    @patch.dict(sys.modules, {"cachetools": None})
    @patch("libumccr.utils.load_package_if_found")
    def test_get_secret_no_cache(self, load_package_if_found):
        """
        python -m unittest tests.aws.test_libssm.LibSsmUnitTests.test_get_secret_no_cache
        """
        load_package_if_found.return_value = False

        from libumccr.aws import libssm
        libssm.get_secret.cache_clear()
        value = libssm.get_secret(key='my-param-secure')
        logger.info(value)
        self.assertEqual(value, 'Sello')
        self.assertIsNone(sys.modules['cachetools'])

    def test_get_secret(self):
        """
        python -m unittest tests.aws.test_libssm.LibSsmUnitTests.test_get_secret
        """

        from libumccr.aws import libssm
        value = libssm.get_secret(key='my-param-secure')
        logger.info(value)
        self.assertEqual(value, 'Sello')

    def test_get_ssm_param(self):
        """
        python -m unittest tests.aws.test_libssm.LibSsmUnitTests.test_get_ssm_param
        """

        from libumccr.aws import libssm
        value = libssm.get_ssm_param(name='my-param')
        logger.info(value)
        self.assertEqual(value, 'Hello')


class LibSsmIntegrationTests(TestCase):

    @skip
    def test_get_secret(self):
        """
        python -m unittest tests.aws.test_libssm.LibSsmIntegrationTests.test_get_secret
        """
        from libumccr.aws import libssm
        key = "/iap/jwt-token"

        value = libssm.get_secret(key=key)

        self.assertIsNotNone(value)
        self.assertIsInstance(value, str)
        logger.info(value)
