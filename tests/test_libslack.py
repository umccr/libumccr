import os
from datetime import datetime
from unittest import TestCase

from mockito import when, mock, verify, unstub

from libumccr import libslack


class LibSlackUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['SLACK_CHANNEL'] = "#mock"

    def tearDown(self) -> None:
        del os.environ['SLACK_CHANNEL']
        unstub()

    def test_call_slack_webhook(self):
        """
        python -m unittest tests.test_libslack.LibSlackUnitTests.test_call_slack_webhook
        """
        mock_sender = "mock sender"
        mock_topic = "mock topic"
        mock_attachments = [
            {
                "title": "mock attachement",
                "text": "test",
            },
            {
                "title": "datetime",
                "text": str(datetime.now()),
            },
        ]
        mock_response = mock(libslack.http.client.HTTPResponse)
        mock_response.status = 200

        when(libslack.libssm).get_ssm_param(...).thenReturn("mock_webhook_id_123")
        when(libslack.http.client.HTTPSConnection).request(...).thenReturn('ok')
        when(libslack.http.client.HTTPSConnection).getresponse(...).thenReturn(mock_response)

        status = libslack.call_slack_webhook(mock_sender, mock_topic, mock_attachments)
        self.assertEqual(200, status)
        verify(libslack.libssm, times=1).get_ssm_param(...)
