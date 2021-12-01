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
    response2 = ec2.allocate_address(
        TagSpecifications=[
            {
                'ResourceType': 'elastic-ip',
                            'Tags': [
                    {
                        'Key': 'string',
                        'Value': EC2InstanceId
                    },
                ]
            },
        ]
    )
    
    eip=response2['AllocationId']
    
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
    responsex = ec2.modify_network_interface_attribute(Attachment={'AttachmentId': eni_attach_id,'DeleteOnTermination': True},
NetworkInterfaceId=eni,)

    #print(response1)
    
    
    ##Associate free EIP to ENI
    ec2 = boto3.client('ec2')
    response3 = ec2.associate_address(
        AllocationId=eip,
        NetworkInterfaceId=eni,
    )
    
    
    ##Detach from instance##
    ##Disassociate EIP##
    ##Delete ENI##
