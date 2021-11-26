#!/usr/bin/python3
import boto3
from pprint import pprint
import time
import json
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc


ec2 = boto3.client('ec2')
response = ec2.describe_network_interfaces()

pprint(response['NetworkInterfaces'])


