#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint

ec2 = boto3.client('ec2')
    
EC2InstanceId="i-0257164da8a87692b"
response = ec2.describe_network_interfaces(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [
                EC2InstanceId,
            ]
        },
    ],
)
#pprint(response)
for each_nic in response['NetworkInterfaces']:
    try:
      eni_assoc_this=each_nic['Association']['AssociationId']
      eni_alloc_this=each_nic['Association']['AllocationId']
      eni_public_ip=each_nic['Association']['PublicIp']
      #response2 = ec2.disassociate_address(AssociationId=eni_assoc_this)
      pprint(eni_assoc_this)
      pprint(eni_public_ip)
    except KeyError:
      pprint("Ok")

