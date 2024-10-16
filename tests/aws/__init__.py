import logging
from unittest import TestCase

from mockito import unstub

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class AWSTestCase(TestCase):

    def setUp(self) -> None:
        super(AWSTestCase, self).setUp()

    def tearDown(self) -> None:
        unstub()
