import boto3

route_table_id = 'rtb-0d1ef50a7fd4cb96b'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id
)