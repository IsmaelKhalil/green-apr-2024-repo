import boto3

internet_gateway_id = 'igw-0ee34eaf7c322bde4'
vpc_id = 'vpc-03f84fa5c1431280f'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)