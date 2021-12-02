#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc

client = boto3.client('autoscaling')

response = client.complete_lifecycle_action(
    LifecycleHookName='DetachLC',
    AutoScalingGroupName='MyASG',
    LifecycleActionResult='CONTINUE',
    InstanceId="i-042fa8f1094bfc753"
)

