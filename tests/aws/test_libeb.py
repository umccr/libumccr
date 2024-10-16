from datetime import datetime

import boto3
from botocore.stub import Stubber
from libumccr import aws
from mockito import when

from libumccr.aws import libeb
from tests.aws import AWSTestCase, logger


class LibEBUnitTests(AWSTestCase):

    def setUp(self):
        super(LibEBUnitTests, self).setUp()
        mock_eb_client = boto3.client('events', region_name='us-east-1')
        self.stubber = Stubber(mock_eb_client)
        self.stubber.activate()
        when(aws).eb_client(...).thenReturn(mock_eb_client)
        when(libeb).eb_client(...).thenReturn(mock_eb_client)

    def test_eb_client(self):
        """
        python -m unittest tests.aws.test_libeb.LibEBUnitTests.test_eb_client
        """
        client = libeb.eb_client()
        logger.info(client)
        logger.info(dir(client))
        self.assertIsNotNone(client)

    def test_get_event_buses(self):
        """
        python -m unittest tests.aws.test_libeb.LibEBUnitTests.test_get_event_buses
        """
        self.stubber.add_response('list_event_buses', {
            'EventBuses': [
                {
                    'Name': 'string',
                    'Arn': 'string',
                    'Description': 'string',
                    'Policy': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        })

        resp = libeb.get_event_buses()
        logger.info(resp)
        self.assertIsNotNone(resp)

    def test_emit_events(self):
        """
        python -m unittest tests.aws.test_libeb.LibEBUnitTests.test_emit_events
        """
        self.stubber.add_response('put_events', {
            'FailedEntryCount': 123,
            'Entries': [
                {
                    'EventId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        })

        resp = libeb.emit_events([
            {
                "Time": datetime(2015, 1, 1),
                "Source": "string",
                "Resources": [
                    "string",
                ],
                "DetailType": "string",
                "Detail": "string",
                "EventBusName": "string",
                "TraceHeader": "string"
            },
        ])
        logger.info(resp)
        self.assertIsNotNone(resp)
        self.assertIn("FailedEntryCount", resp)

    def test_emit_event(self):
        """
        python -m unittest tests.aws.test_libeb.LibEBUnitTests.test_emit_event
        """
        self.stubber.add_response('put_events', {
            'FailedEntryCount': 123,
            'Entries': [
                {
                    'EventId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        })

        resp = libeb.emit_event(
            {
                "Time": datetime(2015, 1, 1),
                "Source": "string",
                "Resources": [
                    "string",
                ],
                "DetailType": "string",
                "Detail": "string",
                "EventBusName": "string",
                "TraceHeader": "string"
            }
        )
        logger.info(resp)
        self.assertIsNotNone(resp)
        self.assertIn("FailedEntryCount", resp)

    def test_dispatch_events(self):
        """
        python -m unittest tests.aws.test_libeb.LibEBUnitTests.test_dispatch_events
        """
        self.stubber.add_response('put_events', {
            'FailedEntryCount': 123,
            'Entries': [
                {
                    'EventId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        })
        self.stubber.add_response('put_events', {
            'FailedEntryCount': 123,
            'Entries': [
                {
                    'EventId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        })

        mock_entries = []
        for n in range(20):
            mock_entries.append(
                {
                    "Time": datetime.now(),
                    "Source": f"string{n}",
                    "Resources": [
                        f"string{n}",
                    ],
                    "DetailType": f"string{n}",
                    "Detail": f"string{n}",
                    "EventBusName": f"string{n}",
                    "TraceHeader": f"string{n}"
                }
            )

        resp = libeb.dispatch_events(mock_entries)
        logger.info("-" * 48)
        logger.info(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(2, len(resp))
