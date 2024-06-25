import boto3
import os

key_name = 'IsmaelKhalil_LUIT'
file_name = 'IsmaelKhalil_LUIT.pem'

ec2 = boto3.client('ec2')

response = ec2.create_key_pair(
    KeyName=key_name
)

with open(file_name, 'w') as f:
    f.write(response['KeyMaterial'])

os.chmod(file_name, 0o400)