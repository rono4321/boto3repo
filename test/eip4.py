#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc

azname="ap-south-1b"
if(azname == "ap-south-1a"):
  subnet1="subnet-0098aab3a90b5f387"
  subnet2="subnet-01ff06d390834cd47"
  print(subnet1)
  print(subnet2)
if(azname == "ap-south-1b"):
  subnet1="subnet-01b3c41bc2906314a"
  subnet2="subnet-0ac522d54a3490987"
  print(subnet1)
  print(subnet2)

