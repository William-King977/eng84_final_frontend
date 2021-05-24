# Final Project - Front End

> Dev branch

## Introduction
The aim of this project is to create a simple service that can scrape useful data from ITJobswatch website and display the current top 30 jobs.
Our app is created with Flask microframework and is divided into three sections:
- Home
- Our Team
- Top 30 Jobs

## Documentation
Requirements:
- Python 3.x+

Make sure the requirements are installed in your Python environment (or virtual environment):
```
python -m pip install -r requirements.txt
```

To run the application:
```
python app.py
```

The above command will run a localhost server on port 8000 on your machine. To view the app, open any browser and enter `127.0.0.1:8000` or `localhost:8000` as the URL.


## Environment variables
The application tries to get a data file from an S3 bucket. To get the data, the `boto3` module is used. However, the module requires some environment variables to be set in order to work correctly. Specifically:
- `AWS_ACCESS_KEY_ID`: Access key for AWS IAM role
- `AWS_SECRET_ACCESS_KEY`: Secret key for AWS IAM role
- `AWS_BUCKET`: Name of bucket in S3
- `AWS_REGION`: Region of S3 bucket
- `FILEPATH_JOBS`: Path of file in bucket
