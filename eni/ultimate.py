#!/usr/bin/python3
import sys
import boto3
from pprint import pprint


##Find free EIP
ec2 = boto3.client('ec2')
response2 = ec2.describe_addresses()
if not response2['Addresses']:
  print("No EIP available in Pool")
  exit(0)

eip_list=[]
for each_eip in response2['Addresses']:
  try:
    ccc=each_eip['AssociationId']
  except KeyError:
    eip_list.append(each_eip['AllocationId'])
# eip_list here is the list of free eip
#pprint(eip_list)
if not eip_list:
  print("No Free EIP available in Pool")
  exit(0)

##Create ENI
ec2 = boto3.client('ec2')
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
ec2 = boto3.client('ec2')
response3 = ec2.associate_address(
    AllocationId=eip_list[0],
    NetworkInterfaceId=eni,
)


##Detach from instance##
##Disassociate EIP##
##Delete ENI##
