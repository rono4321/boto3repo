#!/usr/bin/python3
import boto3
import datetime
from pprint import pprint
from dateutil.tz import tzutc
ec2 = boto3.client('ec2')

eni_list=[]
eni_attach=[]
eni_assoc=[]
eni_name="PythonENILam"
enic={'NetworkInterfaces': [{'Association': {'AllocationId': 'eipalloc-0dd373dcce7ca80cb', 'AssociationId': 'eipassoc-0163a8018056c9f1e', 'IpOwnerId': '612961644341', 'PublicDnsName': '', 'PublicIp': '3.7.105.103'}, 'Attachment': {'AttachTime': datetime.datetime(2021, 11, 25, 16, 20, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0618046c2ace1271d', 'DeleteOnTermination': False, 'DeviceIndex': 1, 'NetworkCardIndex': 0, 'InstanceId': 'i-03c9927dfd879478f', 'InstanceOwnerId': '612961644341', 'Status': 'attached'}, 'AvailabilityZone': 'ap-south-1b', 'Description': 'PythonENILam', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-084d045efc41c9924'}], 'InterfaceType': 'interface', 'Ipv6Addresses': [], 'MacAddress': '0a:39:60:eb:d1:44', 'NetworkInterfaceId': 'eni-0dc39d1c603aeb74c', 'OwnerId': '612961644341', 'PrivateIpAddress': '10.0.1.35', 'PrivateIpAddresses': [{'Association': {'AllocationId': 'eipalloc-0dd373dcce7ca80cb', 'AssociationId': 'eipassoc-0163a8018056c9f1e', 'IpOwnerId': '612961644341', 'PublicDnsName': '', 'PublicIp': '3.7.105.103'}, 'Primary': True, 'PrivateIpAddress': '10.0.1.35'}], 'RequesterId': 'AROAY5N24N422AP6OTMEE:NetworkFunction', 'RequesterManaged': False, 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-0e2856fd01e72d3fc', 'TagSet': [], 'VpcId': 'vpc-01adf6980cdcb3bb2'}, {'Attachment': {'AttachTime': datetime.datetime(2021, 11, 25, 16, 19, 25, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-011bfee8ac3087ecb', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'NetworkCardIndex': 0, 'InstanceId': 'i-03c9927dfd879478f', 'InstanceOwnerId': '612961644341', 'Status': 'attached'}, 'AvailabilityZone': 'ap-south-1b', 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-084d045efc41c9924'}], 'InterfaceType': 'interface', 'Ipv6Addresses': [], 'MacAddress': '0a:01:93:cb:ba:d8', 'NetworkInterfaceId': 'eni-04519a7ba7cd24169', 'OwnerId': '612961644341', 'PrivateIpAddress': '10.0.1.231', 'PrivateIpAddresses': [{'Primary': True, 'PrivateIpAddress': '10.0.1.231'}], 'RequesterManaged': False, 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-0e2856fd01e72d3fc', 'TagSet': [], 'VpcId': 'vpc-01adf6980cdcb3bb2'}], 'ResponseMetadata': {'RequestId': 'bf8dd395-5d2f-4842-a717-41fa83f664f7', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'bf8dd395-5d2f-4842-a717-41fa83f664f7', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '4538', 'date': 'Thu, 25 Nov 2021 16:22:28 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
for each_nic in enic['NetworkInterfaces']:
  desc=each_nic['Description']
  if desc != None and eni_name in desc:
    print("Found!")
    eni_list.append(each_nic['NetworkInterfaceId'])
    eni_attach.append(each_nic['Attachment']['AttachmentId'])
    eni_assoc.append(each_nic['Association']['AssociationId'])
  else:
    print("Not found!")

pprint(eni_list)
pprint(eni_attach)
pprint(eni_assoc)

for each_eni_attach in eni_attach:
  print(each_eni_attach)
  #response = ec2.detach_network_interface(AttachmentId=each_eni_attach,Force=True|False)

for each_eni_assoc in eni_assoc:
  print(each_eni_assoc)
  response = ec2.disassociate_address(AssociationId=each_eni_assoc)
