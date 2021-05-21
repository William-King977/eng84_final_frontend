from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/meet_team")
def meet_team():
    return "Hello, Meet our team!"


@app.route("/data")
def data():
    return "IT JOB WATCH!"


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
