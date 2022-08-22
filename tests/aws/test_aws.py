import logging
from unittest import TestCase, skip

from libumccr import aws

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LibAwsUnitTests(TestCase):

    def test_get_available_services(self):
        """
        python -m unittest tests.aws.test_aws.LibAwsUnitTests.test_get_available_services
        """

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html

        services = aws.session().get_available_services()
        logger.info(services)
        self.assertIsNotNone(services)


class LibAwsIntegrationTests(TestCase):
    """You need to have AWS active session to run these tests
    export AWS_PROFILE=dev
    """

    @skip
    def test_srv_discovery_client(self):
        """
        python -m unittest tests.aws.test_aws.LibAwsIntegrationTests.test_srv_discovery_client
        """
        srv_discovery_client = aws.srv_discovery_client()
        services = srv_discovery_client.list_services()
        logger.info(services)
        self.assertIsNotNone(services)

    @skip
    def test_stepfn_client(self):
        """
        python -m unittest tests.aws.test_aws.LibAwsIntegrationTests.test_stepfn_client
        """
        stepfn_client = aws.stepfn_client()
        state_machines = stepfn_client.list_state_machines()
        logger.info(state_machines)
        self.assertIsNotNone(state_machines)

    @skip
    def test_athena_client(self):
        """
        python -m unittest tests.aws.test_aws.LibAwsIntegrationTests.test_athena_client
        """
        athena_client = aws.athena_client()
        work_groups = athena_client.list_work_groups()
        logger.info(work_groups)
        self.assertIsNotNone(work_groups)
