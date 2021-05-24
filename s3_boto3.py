import csv
import boto3
import botocore
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


# Returns the file contents from the file that was fetched from S3
def collect_data():
    jobs_filename = "ItJobsWatchTop30.csv"
    # source_path = jobs_filename  # location on S3
    # local_file_path = jobs_filename  # location to download the file to

    # Fetch the CSV file from S3
    try:
        # TODO: check if downloaded correctly
        download_s3_file(source=jobs_filename, destination=jobs_filename)
    # Credentials not found, bucket doesn't exist, or file not found
    except (TypeError, botocore.exceptions.ClientError):
        print(f"{jobs_filename} can't be located in the S3 bucket or credentials failed. Using local file.")
    finally:
        try:
            with open(jobs_filename, newline='', encoding='ISO-8859-1') as f:
                reader = csv.reader(f, delimiter=',')
                context = list(reader)
        # File cannot be located in the local file path
        except FileNotFoundError:
            print('Local file not found.')
            context = f"{jobs_filename} can't be located in the S3 bucket or your local file path."
        return context
