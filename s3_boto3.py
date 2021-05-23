import boto3
import os

# Changed to os.getenv to return None

AWS_ACCESS = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET = os.getenv('AWS_BUCKET')
REGION = os.getenv('AWS_REGION')
FILEPATH = os.getenv("FILEPATH_JOBS")

s3 = boto3.client(
    # Connecting to AWS S3 with environment variable credentials
    's3',
    aws_access_key_id=AWS_ACCESS,
    aws_secret_access_key=AWS_SECRET,
)

# bucket_name = "eng84-william-s3"  # needs to change
# region = "eu-west-1"


# Fetch file from S3
# Change to key value arguments (not positional)
# Prefer environment variable for source.
def download_s3_file(*, destination, source=FILEPATH):
    # Changed filename to be included in source path
    # Default value for destination is current dir (?)
    s3.download_file(BUCKET, source, destination)
