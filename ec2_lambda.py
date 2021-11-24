#!/usr/bin/python3
from pprint import pprint
import json
event={'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:ap-south-1:612961644341:Launch:0e931568-231a-4e46-9cd8-e90c2cfd19e2', 'Sns': {'Type': 'Notification', 'MessageId': '34ed5379-6b01-52b6-a3db-0961209a7d25', 'TopicArn': 'arn:aws:sns:ap-south-1:612961644341:Launch', 'Subject': 'Auto Scaling: launch for group "MyASG"', 'Message': '{"Origin":"EC2","Destination":"AutoScalingGroup","Progress":50,"AccountId":"612961644341","Description":"Launching a new EC2 instance: i-0f3206ca62b26d37a","RequestId":"c465f549-3846-6acb-e6f9-28891b09ad3f","EndTime":"2021-11-24T14:16:59.385Z","AutoScalingGroupARN":"arn:aws:autoscaling:ap-south-1:612961644341:autoScalingGroup:84f356fc-11ea-4c44-8f21-7903f71ff38c:autoScalingGroupName/MyASG","ActivityId":"c465f549-3846-6acb-e6f9-28891b09ad3f","StartTime":"2021-11-24T14:16:27.802Z","Service":"AWS Auto Scaling","Time":"2021-11-24T14:16:59.385Z","EC2InstanceId":"i-0f3206ca62b26d37a","StatusCode":"InProgress","StatusMessage":"","Details":{"Subnet ID":"subnet-0e2856fd01e72d3fc","Availability Zone":"ap-south-1b"},"AutoScalingGroupName":"MyASG","Cause":"At 2021-11-24T14:16:26Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 1.","Event":"autoscaling:EC2_INSTANCE_LAUNCH"}', 'Timestamp': '2021-11-24T14:16:59.429Z', 'SignatureVersion': '1', 'Signature': 'FofcS2itsvcyP+lFziMqm8Lu842M7Sd1xPzRp1UEk+s5NYzvF/W5KM+HNUhIkntT8eCC2D6tgBomUWjK3NPttujobxsAZ+EwQiuCF5t5gsMENT+1Z9SWzCnofO80A/XHYKpmU170cvCsywExF2ghDrJgsa+3tE8TYAy7ejDqqntZgqoRB87h7KlYWy5AQcFrNeUaK3jowU3EbHqfY3ubfcc84VY2M1sOCaWkEuWb4J/LlNlh5E+V16kwb7w8nNbN0/jzGTw8TOQcSgcRzdrGAN0ksxidbNIEV6ANH+bqJbbQHSlLslXoaw8Tbq04BAZDMm4+5tsYNkcynfGMpVnysw==', 'SigningCertUrl': 'https://sns.ap-south-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem', 'UnsubscribeUrl': 'https://sns.ap-south-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-south-1:612961644341:Launch:0e931568-231a-4e46-9cd8-e90c2cfd19e2', 'MessageAttributes': {}}}]}
for each_records in (event['Records']):
  people=each_records['Sns']
  for p_id, p_info in people.items():
      if(p_id=="Message"):
        x=json.loads(p_info)
        print(x["EC2InstanceId"])
        print(x["Details"]["Subnet ID"])
        print(x["Details"]["Availability Zone"])
  
