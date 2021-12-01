#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc
ec2 = boto3.client('ec2')

response = {'PublicIp': '65.1.251.90', 'AllocationId': 'eipalloc-0f4e0ae06dcc399f3', 'PublicIpv4Pool': 'amazon', 'NetworkBorderGroup': 'ap-south-1', 'Domain': 'vpc', 'ResponseMetadata': {'RequestId': 'a636da81-f049-4739-a882-0dd8e62f779d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a636da81-f049-4739-a882-0dd8e62f779d', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '427', 'date': 'Wed, 01 Dec 2021 16:15:43 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
 
pprint(response['AllocationId'])
