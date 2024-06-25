import boto3

session = boto3.session()

#Either method here will work.
s3 = boto3.client('s3')
s3 = session.client('s3')

#Either method here will work as well. 
s3 = boto3.resource('s3')
s3 = session.resource('s3')