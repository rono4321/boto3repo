#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc
ec2 = boto3.client('ec2')
EC2InstanceId = "MyInstance"
response = ec2.allocate_address(
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip', 
			'Tags': [
                {
                    'Key': 'string',
                    'Value': EC2InstanceId
                },
            ]
        },
    ]
)
