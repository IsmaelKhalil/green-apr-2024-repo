import boto3

vpc_id = 'vpc-03f84fa5c1431280f'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)