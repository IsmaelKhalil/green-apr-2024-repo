import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    return response

def delete_objects(client, bucket, key):
    
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    keys = [key for key in keys if '/' not in key[len(prefix):]]
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    return response

if __name__ == '__main__':
    s3 = boto3.client('s3')
    bucket = 'ikhalil-boto3-20240522'
    prefix='folder/folder_a/'
    keys = list_object_keys(s3, bucket, prefix=prefix)
    delete_objects_non_recursive(s3, bucket, keys, prefix)
