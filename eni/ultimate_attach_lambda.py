import json
import boto3

def lambda_handler(event, context):
			
    EC2InstanceId=event['detail']['EC2InstanceId']
    
    ec2 = boto3.client('ec2')
    response21 = ec2.describe_instances(
    
        InstanceIds=[
            EC2InstanceId,
        ]
    )
    
    for reservation in response21['Reservations']:
      for inst in reservation['Instances']:
        az_name=inst['Placement']['AvailabilityZone']
			
    for reservation2 in response21['Reservations']:
      for inst1 in reservation['Instances']:
        subnet_id=inst1['SubnetId']

    if(az_name == "ap-south-1a"):
      subnet1="subnet-0098aab3a90b5f387"
      subnet2="subnet-01ff06d390834cd47"
    if(az_name == "ap-south-1b"):
      subnet1="subnet-01b3c41bc2906314a"
      subnet2="subnet-0ac522d54a3490987"
			
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
    response = ec2.create_network_interface(
        Description='PythonENILam',
        Groups=[
            'sg-084d045efc41c9924',
        ],
        SubnetId=subnet1,
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
	
    response3 = ec2.associate_address(
        AllocationId=eip,
        NetworkInterfaceId=eni,
    )


    ##Create ENI
    response = ec2.create_network_interface(
        Description='PythonENILam2',
        Groups=[
            'sg-084d045efc41c9924',
        ],
        SubnetId=subnet2,
    )
    eni2=response['NetworkInterface']['NetworkInterfaceId']
    
    ##Attach ENI to instance
    response1 = ec2.attach_network_interface(
        DeviceIndex=2,
        InstanceId=EC2InstanceId,
        NetworkInterfaceId=eni2
    )

    eni_attach_id2=response1['AttachmentId']
    responsex = ec2.modify_network_interface_attribute(Attachment={'AttachmentId': eni_attach_id2,'DeleteOnTermination': True},
NetworkInterfaceId=eni2,)
    
    autoscaling = boto3.client('autoscaling')
    response = autoscaling.complete_lifecycle_action(
        LifecycleHookName='LaunchLC',
        AutoScalingGroupName='MyASG',
        LifecycleActionResult='CONTINUE',
        InstanceId=EC2InstanceId
    )    
    
    ##Detach from instance##
    ##Disassociate EIP##
    ##Delete ENI##
	
	
