#!/usr/bin/python3
import sys
import boto3


ec2 = boto3.client('ec2')
response1 = ec2.attach_network_interface(
    DeviceIndex=1,
    InstanceId='i-02859d54d578f719a',
    NetworkInterfaceId='eni-0aba64a9d32ff4084'
)
print(response1)
