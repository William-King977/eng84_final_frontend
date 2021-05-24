import csv
import requests

S3_FILE_URL = "https://eng84-final-project.s3-eu-west-1.amazonaws.com/ItJobsWatchTop30.csv"
JOBS_FILENAME = "ItJobsWatchTop30.csv"

# Fetches the CSV file from the S3 bucket
def collect_data_url():
    s3_request = requests.get(S3_FILE_URL)

    # If the file is found.
    if s3_request: 
        s3_content = s3_request.content.decode('ISO-8859-1')
        reader = csv.reader(s3_content.splitlines(), delimiter=',')
        context = list(reader)[0:30]
    # If the file can't be found (no response from the URL)
    else:
        context = "The file can't be located in the S3 bucket."
    return context


# Fetch the CSV file from the local machine
def collect_data_local():
    try:
        with open(JOBS_FILENAME, newline='', encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=',')
            context = list(reader)[0:30]
    # File cannot be located in the local file path
    except FileNotFoundError:
        print('Local file not found.')
        context = f"{JOBS_FILENAME} can't be located on your local file path."
    return context
