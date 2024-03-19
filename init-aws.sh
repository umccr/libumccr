#!/bin/bash
awslocal s3 mb s3://my-bucket
awslocal sqs create-queue --region ap-southeast-2 --queue-name my-queue
awslocal ssm put-parameter --region ap-southeast-2 --name my-param --type String --value 'Hello'
awslocal ssm put-parameter --region ap-southeast-2 --name my-param-secure --type SecureString --value 'Sello'  # pragma: allow-secret
awslocal secretsmanager create-secret --region ap-southeast-2 --name MyTestSecret --secret-string "HealTheWorld"  # pragma: allow-secret
awslocal secretsmanager create-secret --region ap-southeast-2 --name MyTestSecretJson --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"  # pragma: allow-secret
