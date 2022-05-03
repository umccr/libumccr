import logging
from unittest import TestCase

from libumccr.aws import liblambda

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LibLambdaUnitTests(TestCase):

    def test_transpose_fn_url_event(self):
        """
        python -m unittest tests.aws.test_liblambda.LibLambdaUnitTests.test_transpose_fn_url_event
        """
        mock_event = {
            "version": "2.0",
            "routeKey": "$default",
            "headers": {
                "content-type": "application/json",
            },
            "queryStringParameters": {
                "subject_id": "SBJ00001"
            },
            "requestContext": {
                "http": {
                    "method": "POST",
                }
            },
            "body": {"subject_id": "SBJ00001"},
            "isBase64Encoded": False,
        }
        event = liblambda.transpose_fn_url_event(event=mock_event)
        logger.info(event)
        self.assertEqual(event['subject_id'], "SBJ00001")

    def test_transpose_fn_url_event_merged(self):
        """
        python -m unittest tests.aws.test_liblambda.LibLambdaUnitTests.test_transpose_fn_url_event_merged
        """
        mock_event = {
            "version": "2.0",
            "routeKey": "$default",
            "headers": {
                "content-type": "application/json",
            },
            "queryStringParameters": {
                "library_id": "L9900111"
            },
            "requestContext": {
                "http": {
                    "method": "POST",
                }
            },
            "body": {"subject_id": "SBJ00001"},
            "isBase64Encoded": False,
        }
        event = liblambda.transpose_fn_url_event(event=mock_event)
        logger.info(event)
        self.assertEqual(event['subject_id'], "SBJ00001")
        self.assertEqual(event['library_id'], "L9900111")

    def test_transpose_fn_url_event_passthrough(self):
        """
        python -m unittest tests.aws.test_liblambda.LibLambdaUnitTests.test_transpose_fn_url_event_passthrough
        """
        mock_event = {
            "subject_id": "SBJ00001",
            "version": "2.0",
        }
        event = liblambda.transpose_fn_url_event(event=mock_event)
        logger.info(event)
        self.assertEqual(mock_event, event)
