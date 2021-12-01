#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc
ec2 = boto3.client('ec2')
EC2InstanceId = "MyInstance"

response = ec2.describe_addresses(
    Filters=[{'Name':'tag:string', 'Values':["i-0e938a4d6e11477d1"]},
          ]


)

AllocationId=response['Addresses'][0]['AllocationId']
response2 = ec2.release_address(AllocationId=AllocationId)

