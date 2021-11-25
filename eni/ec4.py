#!/usr/bin/python3
import sys
import boto3
from pprint import pprint


ec2 = boto3.client('ec2')
response = ec2.associate_address(
    AllocationId='eipalloc-0cf713d4a20e99b14',
    NetworkInterfaceId='eni-06d9cd2eade63189a',
)

