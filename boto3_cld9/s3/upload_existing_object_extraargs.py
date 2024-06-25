import boto3

s3 = boto3.client('s3')

s3.upload_file('boto3_cld9/test_text.txt', 'ikhalil-boto3-20240522', 'test_text.txt', ExtraArgs={'ContentType': 'text/plain'})