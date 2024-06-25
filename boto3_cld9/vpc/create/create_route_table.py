import boto3

ec2 = boto3.client('ec2')

cidr_block = '12.0.1.0/24'
vpc_id = 'vpc-03f84fa5c1431280f'

route_table = ec2.create_route_table(
    VpcId=vpc_id,
)

print(route_table['RouteTable']['RouteTableId'])