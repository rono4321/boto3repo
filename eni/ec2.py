#!/usr/bin/python3
import sys
import boto3


ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-0566bc8f806225570'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-0566bc8f806225570'])
print(response)
