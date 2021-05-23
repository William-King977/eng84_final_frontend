from flask import Flask, render_template
# import s3_boto3
# from s3_boto3 import download_s3_file
import csv
import team

# Set as variables so that they can be easily changed
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

# Initialise flask app
app = Flask(__name__)


@app.route("/")
def index():
    # Include team member names and teams
    context = team.team
    # return render_template("home.html", job_list=collect_data(), context=context)
    return render_template('home.html', context=context)


@app.route("/data")
def data():
	return render_template('top30.html')
    # return "IT JOB WATCH!"


@app.route("/top30-test")  # Remove this line once Top 30 Jobs table has been added to base.html
def collect_data():
    jobs_filename = "ItJobsWatchTop30.csv"
    # source_path = jobs_filename  # location on S3
    # local_file_path = jobs_filename  # location to download the file to

    # Fetch the CSV file from S3
    try:
        # TODO: check if downloaded correctly
        download_s3_file(source=jobs_filename, destination=jobs_filename)
    # Credentials not found, or file not found
    except (KeyError, FileNotFoundError):
        print(f'or credentials failed. Using local')
    finally:
        try:
            with open(jobs_filename, newline='',  encoding='ISO-8859-1') as f:
                reader = csv.DictReader(f, delimiter=',')
                context = list(reader)
        # file cannot be located on s3 bucket or local
        except FileNotFoundError:
            print('Local file not found')
            context = f"{jobs_filename} can't be located in the S3 bucket or your local file path."
        return render_template(
                "top30-test.html", job_list=context)


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT, host=HOST)


# @app.route("/meet_team")
# def meet_team():
#     return "Hello, Meet our team!"
