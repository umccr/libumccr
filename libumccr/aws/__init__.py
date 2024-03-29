# -*- coding: utf-8 -*-
"""aws package

Factory init module for creating boto3 client and resource to interface AWS services
"""
import boto3


def session(**kwargs):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html

    :param kwargs:
    :return:
    """
    return boto3.session.Session(**kwargs)


def client(service_name, **kwargs):
    return session().client(service_name=service_name, **kwargs)


def resource(service_name, **kwargs):
    return session().resource(service_name=service_name, **kwargs)


def s3_client(**kwargs):
    return client('s3', **kwargs)


def sqs_client(**kwargs):
    return client('sqs', **kwargs)


def ssm_client(**kwargs):
    return client('ssm', **kwargs)


def sm_client(**kwargs):
    return client('secretsmanager', **kwargs)


def lambda_client(**kwargs):
    return client('lambda', **kwargs)


def stepfn_client(**kwargs):
    return client('stepfunctions', **kwargs)


def srv_discovery_client(**kwargs):
    return client('servicediscovery', **kwargs)


def athena_client(**kwargs):
    return client('athena', **kwargs)


def eb_client(**kwargs):
    return client('events', **kwargs)
