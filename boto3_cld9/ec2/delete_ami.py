import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-0ba3b566b2e0196f3',
)

print(response)