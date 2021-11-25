#!/usr/bin/python3
import sys
import boto3
from pprint import pprint


ec2 = boto3.client('ec2')
response = ec2.describe_addresses()
#pprint(response['Addresses'])
if not response['Addresses']:
  print("No EIP available in Pool")
  exit(0)
eip_list=[]
for each_eip in response['Addresses']:
  try:
    ccc=each_eip['AssociationId']
  except KeyError:
    eip_list.append(each_eip['AllocationId'])
# eip_list here is the list of free eip
#pprint(eip_list)
if not eip_list:
  print("No Free EIP available in Pool")
  exit(0)

