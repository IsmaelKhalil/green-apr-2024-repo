import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-04d61dd225f11da04',
    Name='NewEC2Instance',
)

print(response['ImageId'])