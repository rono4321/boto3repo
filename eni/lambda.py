#!/usr/bin/python3
import json
import boto3
ec2 = boto3.client('ec2')
response2 = ec2.describe_addresses()
if not response2['Addresses']:
  print("No EIP available in Pool")
  exit(0)


