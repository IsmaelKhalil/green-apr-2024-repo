import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='ikhalil-boto3-20240522'

)

print(response)