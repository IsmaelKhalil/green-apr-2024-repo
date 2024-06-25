import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_types(
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'false',
            ]
        },
    ],
)

for instance_type in response['InstanceTypes']:
    print(instance_type['InstanceType'], instance_type['FreeTierEligible'])