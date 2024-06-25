import boto3

s3 = boto3.client('s3')

# Bucket and Key are required. Body isn't, but we are using it since we need to send in the object
with open('boto3_cld9/test_text.txt', 'rb') as f:
    s3.put_object(Bucket='ikhalil-boto3-20240522', Key='test_text.txt', Body=f, ContentType='text/plain')