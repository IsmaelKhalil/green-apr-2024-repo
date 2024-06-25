import boto3

vpc_id = 'vpc-09613a4ee6565162a'

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SecurityGroup-Boto3',
    GroupName='SecurityGroup-Boto3',
    VpcId=vpc_id,
)

print(response['GroupId'])