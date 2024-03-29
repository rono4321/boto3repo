#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc

client = boto3.client('autoscaling')

response = client.complete_lifecycle_action(
    LifecycleHookName='LaunchLC',
    AutoScalingGroupName='MyASG',
    LifecycleActionResult='CONTINUE',
    InstanceId="i-0c96023045f36a6b3"
)

