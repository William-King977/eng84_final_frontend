from flask import Flask, render_template
from s3_boto3 import download_s3_file
import csv

app = Flask(__name__)


@app.route("/")
def index():
    # Include team member names and teams
    context = {
            "front": [
                {
                    "name": "Alexis Othonos",
                    "src": "static/team/alexis.jpg",
                    "role": "Frontend Scrum Master",
                },
                {
                    "name": "Ula Ziolko",
                    "src": "static/team/ula.jpg",
                    "role": "Frontend",
                },
                {
                    "name": "Oleg Negruta",
                    "src": "/static/team/oleg.jpg",
                    "role": "Frontend",
                },

                {
                    "name": "William King",
                    "src": "static/team/will.jpg",
                    "role": "Frontend",
                },
            ],
            "auto": [
                {
                    "name": "Ben Ranson",
                    "src": "static/team/ben.jpg",
                    "role": "Automation Scrum Master",
                },
                {
                    "name": "Saverio Cutrupi",
                    "src": "static/team/savi.jpg",
                    "role": "Automation ",
                },
                {
                    "name": "Isobel Fitt-Conway",
                    "src": "static/team/isobel.jpg",
                    "role": "Automation",
                },
                {
                    "name": "Andrew Asare",
                    "src": "static/team/andrew.jpg",
                    "role": "Automation",
                },

                ],
            "test": [
                {
                    "name": "Arun Panesar",
                    "src": "static/team/arun.jpg",
                    "role": "Testing Scrum Master",
                },
                {
                    "name": "Jordan Clarke",
                    "src": "static/team/jordan.jpg",
                    "role": "Testing Engineer",
                },
                {
                    "name": "Jose Torres",
                    "src": "static/team/jose.jpg",
                    "role": "Testing Engineer",
                },

                ]
            }

    # return render_template("home.html", job_list=collect_data(), context=context)
    return render_template('home.html', context=context)


@app.route("/meet_team")
def meet_team():
    return "Hello, Meet our team!"


@app.route("/data")
def data():
    return "IT JOB WATCH!"


@app.route("/top30-test") # Remove this line once Top 30 Jobs table has been added to base.html
def collect_data():
    jobs_filename = "ItJobsWatchTop30.csv"
    s3_file_path = jobs_filename # location on S3
    local_file_path = jobs_filename # location to download the file to

    # Fetch the CSV file from S3
    try:
        download_s3_file(jobs_filename, s3_file_path, local_file_path)
    except:
        # return f"{jobs_filename} cannot be located in the S3 bucket path: {s3_file_path}, or your local file path cannot be located: {local_file_path}."
        return render_template("top30-test.html", job_list=f"{jobs_filename} cannot be located in the S3 bucket path: {s3_file_path}, or your local file path cannot be located: {local_file_path}.") # Remove this

    # Fetching the downloaded CSV file
    try:
        # Import the CSV and convert it into a list of dictionaries
        with open(local_file_path, newline='') as f:
            reader = csv.DictReader(f, delimiter=',')
            top30_jobs_list = list(reader)

        # return top30_jobs_list
        return render_template("top30-test.html", job_list=top30_jobs_list) # Remove this too
    except:
        # return f"{jobs_filename} cannot be located on your local machine path: {local_file_path}."
        return render_template("top30-test.html", job_list=f"{jobs_filename} cannot be located on your local machine path: {local_file_path}.") # Remove this too


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
