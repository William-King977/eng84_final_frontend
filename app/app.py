from flask import Flask, render_template
import data_collector
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

    # Fetch the data from S3
    data = data_collector.collect_data_url()
    return render_template("home.html", context=list(team.team.values()), data=data)


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT, host=HOST)


# @app.route("/meet_team")
# def meet_team():
#     return "Hello, Meet our team!"


# @app.route("/data")
# def data():
#     return "IT JOB WATCH!"
