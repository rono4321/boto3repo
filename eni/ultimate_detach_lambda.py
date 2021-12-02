import json
import boto3
import time
ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    # TODO implement
    EC2InstanceId=event['detail']['EC2InstanceId']
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
    if not response['NetworkInterfaces']:
        response = ec2.describe_addresses(
            Filters=[{'Name':'tag:string', 'Values':[EC2InstanceId]},
                  ]
        )
        
        AllocationId=response['Addresses'][0]['AllocationId']
        response2 = ec2.release_address(AllocationId=AllocationId)
        print(response2)
    else:
    
        for each_nic in response['NetworkInterfaces']:
            try:
                eni_assoc_this=each_nic['Association']['AssociationId']
                eni_alloc_this=each_nic['Association']['AllocationId']
                response2 = ec2.disassociate_address(AssociationId=eni_assoc_this)
                time.sleep(20)
                print(eni_alloc_this)
                print(eni_assoc_this)
                response3 = ec2.release_address(AllocationId=eni_alloc_this)
                print(response3)
            except KeyError:
                print("Ok")
                
        autoscaling = boto3.client('autoscaling')
    
    response = autoscaling.complete_lifecycle_action(
        LifecycleHookName='DetachLC',
        AutoScalingGroupName='MyASG',
        LifecycleActionResult='CONTINUE',
        InstanceId=EC2InstanceId
    )


