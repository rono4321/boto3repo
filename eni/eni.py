#!/usr/bin/python3
import sys
import boto3


ec2 = boto3.client('ec2')
response = ec2.create_network_interface(
    Description='PythonENI',
    Groups=[
        'sg-084d045efc41c9924',
    ],
    SubnetId='subnet-00c38dc0ec5e09e28',
)
print(response)
eni=response['NetworkInterface']['NetworkInterfaceId']
response1 = ec2.attach_network_interface(
    DeviceIndex=1,
    InstanceId='i-0ef409b91c9373561',
    NetworkInterfaceId=eni
)
print(response1)
