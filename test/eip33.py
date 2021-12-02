#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc

event={'version': '0', 'id': 'c442a810-ec16-a742-301d-c28e18e96e01', 'detail-type': 'EC2 Instance-terminate Lifecycle Action', 'source': 'aws.autoscaling', 'account': '612961644341', 'time': '2021-12-02T13:56:43Z', 'region': 'ap-south-1', 'resources': ['arn:aws:autoscaling:ap-south-1:612961644341:autoScalingGroup:84f356fc-11ea-4c44-8f21-7903f71ff38c:autoScalingGroupName/MyASG'], 'detail': {'LifecycleActionToken': '2db34df6-c665-4c6b-8a82-56ab8b09d9b2', 'AutoScalingGroupName': 'MyASG', 'LifecycleHookName': 'DetachLC', 'EC2InstanceId': 'i-07690e756e4f7d989', 'LifecycleTransition': 'autoscaling:EC2_INSTANCE_TERMINATING', 'Origin': 'AutoScalingGroup', 'Destination': 'EC2'}}

#pprint(event)
pprint(event['detail']['EC2InstanceId'])

#client = boto3.client('ec2')

#response = client.describe_instances(
#
#    InstanceIds=[
#        'i-0f346a744ada7fae1',
#    ]
#)
#print(response)
response={'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-0108d6a82a783b352', 'InstanceId': 'i-0f346a744ada7fae1', 'InstanceType': 't2.micro', 'KeyName': 'ppk-key', 'LaunchTime': datetime.datetime(2021, 12, 2, 9, 53, 18, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'ap-south-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-10-0-0-48.ap-south-1.compute.internal', 'PrivateIpAddress': '10.0.0.48', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-00c38dc0ec5e09e28', 'VpcId': 'vpc-01adf6980cdcb3bb2', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2021, 12, 2, 9, 53, 19, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-0c1903a724c0fe457'}}], 'ClientToken': '8d35f5ea-3ffd-1cb4-d7ae-6f019194e120', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2021, 12, 2, 9, 53, 18, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-066f0cfe1040bf45d', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-084d045efc41c9924'}], 'Ipv6Addresses': [], 'MacAddress': '02:54:e3:a7:80:c2', 'NetworkInterfaceId': 'eni-0c021edc358083b99', 'OwnerId': '612961644341', 'PrivateIpAddress': '10.0.0.48', 'PrivateIpAddresses': [{'Primary': True, 'PrivateIpAddress': '10.0.0.48'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-00c38dc0ec5e09e28', 'VpcId': 'vpc-01adf6980cdcb3bb2', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-084d045efc41c9924'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'aws:ec2launchtemplate:version', 'Value': '2'}, {'Key': 'aws:ec2launchtemplate:id', 'Value': 'lt-09c108d218284b429'}, {'Key': 'aws:autoscaling:groupName', 'Value': 'MyASG'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2021, 12, 2, 9, 53, 18, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}}], 'OwnerId': '612961644341', 'RequesterId': '968245739290', 'ReservationId': 'r-0b5f144d8835ac559'}], 'ResponseMetadata': {'RequestId': 'e1f8e0db-fb5d-4b5a-a065-8a1c758bd768', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e1f8e0db-fb5d-4b5a-a065-8a1c758bd768', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '7456', 'date': 'Thu, 02 Dec 2021 09:55:34 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

#for i in response['Reservations']:
#  for j in i['Instances']:
#    pprint(j['SubnetId'])
