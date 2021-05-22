from flask import Flask, render_template
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

    # Import the CSV and convert it into a list of dictionaries
    # with open('static/ItJobsWatchTop30.csv', newline='') as f:
    #     reader = csv.DictReader(f, delimiter=',')
    #     top30_jobs_list = list(reader)
    # return render_template("top30-test.html", job_list=top30_jobs_list, context=context)
    return render_template('home.html', context=context)


@app.route("/meet_team")
def meet_team():
    return "Hello, Meet our team!"


@app.route("/data")
def data():
    return "IT JOB WATCH!"


# Remove once Top 30 Jobs table has been added to base.html
@app.route("/top30-test")
def collect_data():
    # Import the CSV and convert it into a list of dictionaries
    with open('static/ItJobsWatchTop30.csv', newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        top30_jobs_list = list(reader)

    return render_template("top30-test.html", job_list=top30_jobs_list)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
