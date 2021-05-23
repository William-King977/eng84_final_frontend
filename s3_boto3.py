import boto3
import os

# Connecting to AWS with environment variable credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)

bucket_name = "eng84-william-s3" # needs to change
region = "eu-west-1"

# Fetch file from S3
def download_s3_file(filename, s3_path, local_path):
    # Second param is the file location in the S3 bucket
    # Third param is the file location to save the file
    s3.download_file(bucket_name, s3_path, local_path)
