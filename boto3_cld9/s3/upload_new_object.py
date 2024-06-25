import boto3

s3 = boto3.client('s3')

# Bucket and Key are required. Body isn't, but we are using it since we need to send in the object
s3.put_object(Bucket='ikhalil-boto3-20240522', Key='folder/folder_a/folder1/test_text_string.txt', Body='Hey this is a string', ContentType='text/plain')