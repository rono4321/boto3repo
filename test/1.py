#!/usr/bin/python3
import boto3
from pprint import pprint
import json

event={'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:ap-south-1:612961644341:Terminate:5e068bab-8ba8-4f77-82e8-32af574a8111', 'Sns': {'Type': 'Notification', 'MessageId': '96fe668e-ed46-5620-a4bd-3c977191bf6f', 'TopicArn': 'arn:aws:sns:ap-south-1:612961644341:Terminate', 'Subject': 'Auto Scaling: termination for group "MyASG"', 'Message': '{"Origin":"AutoScalingGroup","Destination":"EC2","Progress":50,"AccountId":"612961644341","Description":"Terminating EC2 instance: i-0b4cc4ac47b329297","RequestId":"9147b698-4659-4105-be85-de0cd48e2dd1","EndTime":"2021-11-25T14:15:51.128Z","AutoScalingGroupARN":"arn:aws:autoscaling:ap-south-1:612961644341:autoScalingGroup:84f356fc-11ea-4c44-8f21-7903f71ff38c:autoScalingGroupName/MyASG","ActivityId":"9147b698-4659-4105-be85-de0cd48e2dd1","StartTime":"2021-11-25T14:15:09.391Z","Service":"AWS Auto Scaling","Time":"2021-11-25T14:15:51.128Z","EC2InstanceId":"i-03c9927dfd879478f","StatusCode":"InProgress","StatusMessage":"","Details":{"Subnet ID":"subnet-00c38dc0ec5e09e28","Availability Zone":"ap-south-1a"},"AutoScalingGroupName":"MyASG","Cause":"At 2021-11-25T14:14:55Z a user request update of AutoScalingGroup constraints to min: 0, max: 1, desired: 0 changing the desired capacity from 1 to 0.  At 2021-11-25T14:15:09Z an instance was taken out of service in response to a difference between desired and actual capacity, shrinking the capacity from 1 to 0.  At 2021-11-25T14:15:09Z instance i-0b4cc4ac47b329297 was selected for termination.","Event":"autoscaling:EC2_INSTANCE_TERMINATE"}', 'Timestamp': '2021-11-25T14:15:51.155Z', 'SignatureVersion': '1', 'Signature': 'iWvYxOKMMxoWUPxMQtHYrFbsdH76bqVnG05W1a9n2FTOfmvBFcWvF713tlc1V1ReGhgBn3d+9yVpeX159I1dJmbCF4IHbpnRJ36PE1ObDq0liAT2eARGw+CUeWcQMGTVbS7KcaDpz64TjCgF8Q+05FoadphJz6u4o+32owjflURNa8gsJ4AfMkS0LNUzhtLyRWa5Tm7IEYAvVj89h0ZABsGYXH2R7bZip5xrXs71qKJaapMH3bFhTk0TN9MvVMXjVyd7QX4QQdBkaC4ZpfcVIFyc/q8ieUj54BzTpAHF+xpXbW6gcY7DIuB20WjS6OcopvL3p40owsiVUkWVBqxjmA==', 'SigningCertUrl': 'https://sns.ap-south-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem', 'UnsubscribeUrl': 'https://sns.ap-south-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-south-1:612961644341:Terminate:5e068bab-8ba8-4f77-82e8-32af574a8111', 'MessageAttributes': {}}}]}
#pprint(event)
for each_records in (event['Records']):
  sns_records=each_records['Sns']
  for m_id, m_info in sns_records.items():
      if(m_id=="Message"):
        x=json.loads(m_info)
        EC2InstanceId=x["EC2InstanceId"]
        pprint(EC2InstanceId)

ec2 = boto3.client('ec2')
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
