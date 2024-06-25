import boto3

route_table_id = 'rtb-0d1ef50a7fd4cb96b'
internet_gateway_id = 'igw-0ee34eaf7c322bde4'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id
)