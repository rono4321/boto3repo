#!/usr/bin/python3
from pprint import pprint
#aaa={'NetworkInterface': {'AvailabilityZone': 'ap-south-1b', 'Description': 'PythonENI', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-084d045efc41c9924'}], 'InterfaceType': 'interface', 'Ipv6Addresses': [], 'MacAddress': '0a:07:5f:65:f2:d4', 'NetworkInterfaceId': 'eni-06f659be4975b2551', 'OwnerId': '612961644341', 'PrivateIpAddress': '10.0.1.248', 'PrivateIpAddresses': [{'Primary': True, 'PrivateIpAddress': '10.0.1.248'}], 'RequesterId': 'AIDAY5N24N422ULVT3N6Q', 'RequesterManaged': False, 'SourceDestCheck': True, 'Status': 'pending', 'SubnetId': 'subnet-0e2856fd01e72d3fc', 'TagSet': [], 'VpcId': 'vpc-01adf6980cdcb3bb2'}, 'ResponseMetadata': {'RequestId': '204f6cc0-1a15-4bf9-9194-780d430cfaf5', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '204f6cc0-1a15-4bf9-9194-780d430cfaf5', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1358', 'date': 'Thu, 25 Nov 2021 09:59:22 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
#pprint(aaa['NetworkInterface']['NetworkInterfaceId'])

bbb=[{'AllocationId': 'eipalloc-0cf713d4a20e99b14',
  'Domain': 'vpc',
  'NetworkBorderGroup': 'ap-south-1',
  'PublicIp': '15.207.206.175',
  'PublicIpv4Pool': 'amazon'},
 {'AllocationId': 'eipalloc-052565568f0a40b31',
  'AssociationId': 'eipassoc-09cfc41defe067427',
  'Domain': 'vpc',
  'InstanceId': 'i-0ef409b91c9373561',
  'NetworkBorderGroup': 'ap-south-1',
  'NetworkInterfaceId': 'eni-06d9cd2eade63189a',
  'NetworkInterfaceOwnerId': '612961644341',
  'PrivateIpAddress': '10.0.0.225',
  'PublicIp': '3.109.13.88',
  'PublicIpv4Pool': 'amazon'},
 {'AllocationId': 'eipalloc-03e01bcfbcdea8c63',
  'Domain': 'vpc',
  'NetworkBorderGroup': 'ap-south-1',
  'PublicIp': '3.7.221.74',
  'PublicIpv4Pool': 'amazon'}]

#pprint(bbb)
xxx=[]
for each_eip in bbb:
  try:
    ccc=each_eip['AssociationId']
  except KeyError:
    xxx.append(each_eip['AllocationId'])  

pprint(xxx)
