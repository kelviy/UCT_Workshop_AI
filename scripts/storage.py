import boto3
from botocore.exceptions import NoCredentialsError

def uploadToS3(file_name, bucket, s3_file_name):
    s3 = boto3.client('s3')

    s3.upload_file(file_name, bucket, s3_file_name)
    print(f"Uploaded succesfully File upload as {s3_file_name}")
    return True

local_file_name = 'output.txt'
bucket_name = 'uct-workshop' #name of bucket in aws s3
s3_file_name = 'output.txt'

uploadToS3(local_file_name, bucket_name, s3_file_name)
