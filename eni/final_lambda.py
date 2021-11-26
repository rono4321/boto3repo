import json
import boto3

def lambda_handler(event, context):
    # TODO implement 
    for each_records in (event['Records']):
      sns_records=each_records['Sns']
      for m_id, m_info in sns_records.items():
          if(m_id=="Message"):
            x=json.loads(m_info)
            EC2InstanceId=x["EC2InstanceId"]
            subnet_id=x["Details"]["Subnet ID"]
            az=x["Details"]["Availability Zone"]
    
    ec2 = boto3.client('ec2')
    ##Find free EIP
    response2 = ec2.describe_addresses()
    if not response2['Addresses']:
      print("No EIP available in Pool")
      exit(0)
    
    eip_list=[]
    for each_eip in response2['Addresses']:
      try:
        ccc=each_eip['AssociationId']
      except KeyError:
        eip_list.append(each_eip['AllocationId'])
    # eip_list here is the list of free eip
    #pprint(eip_list)
    if not eip_list:
      print("No Free EIP available in Pool")
      exit(0)
    
    ##Create ENI
    ec2 = boto3.client('ec2')
    response = ec2.create_network_interface(
        Description='PythonENILam',
        Groups=[
            'sg-084d045efc41c9924',
        ],
        SubnetId=subnet_id,
    )
    eni=response['NetworkInterface']['NetworkInterfaceId']
    
    ##Attach ENI to instance
    response1 = ec2.attach_network_interface(
        DeviceIndex=1,
        InstanceId=EC2InstanceId,
        NetworkInterfaceId=eni
    )
    
    eni_attach_id=response1['AttachmentId']
    responsex = ec2.modify_network_interface_attribute(Attachment={'AttachmentId': eni_attach_id,'DeleteOnTermination': True},NetworkInterfaceId=eni,)

    #print(response1)
    
    
    ##Associate free EIP to ENI
    ec2 = boto3.client('ec2')
    response3 = ec2.associate_address(
        AllocationId=eip_list[0],
        NetworkInterfaceId=eni,
    )
    
    
    ##Detach from instance##
    ##Disassociate EIP##
    ##Delete ENI##
