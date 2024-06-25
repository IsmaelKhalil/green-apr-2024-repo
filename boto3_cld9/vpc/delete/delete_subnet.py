import boto3

subnet_id = 'subnet-07fe8bef023456717'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id
)