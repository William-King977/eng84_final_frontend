from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route("/")
def index():
	# with open('static/ItJobsWatchTop30.csv', newline='') as f:
	#     reader = csv.reader(f)
	#     top30_jobs_list = list(reader)
	# return render_template("home.html", job_list=top30_jobs_list)
    return render_template('home.html')


@app.route("/meet_team")
def meet_team():
    return "Hello, Meet our team!"


@app.route("/data")
def data():
    return "IT JOB WATCH!"


# Remove once Top 30 Jobs table has been added to base.html
@app.route("/top30-test")
def collect_data():
	# Import the CSV and convert it into a list
	with open('static/ItJobsWatchTop30.csv', newline='') as f:
	    reader = csv.reader(f)
	    top30_jobs_list = list(reader)

	return render_template("top30-test.html", job_list=top30_jobs_list)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
