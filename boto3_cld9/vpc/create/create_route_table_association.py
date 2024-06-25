import boto3

route_table_id = 'rtb-0d1ef50a7fd4cb96b'
subnet_id = 'subnet-07fe8bef023456717'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(association['AssociationId'])