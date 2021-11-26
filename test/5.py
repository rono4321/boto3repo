#!/usr/bin/python3
import boto3
from pprint import pprint
import json

ec2 = boto3.client('ec2')
response = ec2.modify_network_interface_attribute(
    Attachment={
        'AttachmentId': 'eni-attach-0349bab9d885d331a',
        'DeleteOnTermination': True
    },
    NetworkInterfaceId='eni-0da00fbe417f4908c',
)
print(response)
