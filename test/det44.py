#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint

ec2 = boto3.client('ec2')
    
response = ec2.release_address(AllocationId='eipalloc-06cf0d1ef8399721a')
print(response)
