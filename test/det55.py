#!/usr/bin/python3
import json
import boto3
import time
ec2 = boto3.client('ec2')
# TODO implement
#print(event)
EC2InstanceId="i-0f26d761bce2aa58d"
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
print(response)
for each_nic in response['NetworkInterfaces']:
    try:
        eni_assoc_this=each_nic['Association']['AssociationId']
        eni_alloc_this=each_nic['Association']['AllocationId']
        #response2 = ec2.disassociate_address(AssociationId=eni_assoc_this)
        #print(response2)
        #time.sleep(20)
        print(eni_assoc_this)
        print(eni_alloc_this)
        #response3 = ec2.release_address(AllocationId=eni_alloc_this)
        #print(response3)
    except KeyError:
        print("Ok")
        


