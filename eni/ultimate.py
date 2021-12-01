#!/usr/bin/python3
import sys
import boto3
from pprint import pprint


##Find free EIP
ec2 = boto3.client('ec2')
response2 = ec2.allocate_address()
eip=response2['AllocationId']


##Create ENI
response = ec2.create_network_interface(
    Description='PythonENI',
    Groups=[
        'sg-084d045efc41c9924',
    ],
    SubnetId='subnet-00c38dc0ec5e09e28',
)
eni=response['NetworkInterface']['NetworkInterfaceId']

##Attach ENI to instance
response1 = ec2.attach_network_interface(
    DeviceIndex=1,
    InstanceId='i-0ef409b91c9373561',
    NetworkInterfaceId=eni
)
#print(response1)


##Associate free EIP to ENI
response3 = ec2.associate_address(
    AllocationId=eip,
    NetworkInterfaceId=eni,
)


##Detach from instance##
##Disassociate EIP##
##Delete ENI##
