import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_key_pair(
    KeyName='IsmaelKhalil_LUIT',
)

print(response)