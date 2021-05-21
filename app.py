from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, welcome to the home page!"

@app.route("/meet_team")
def meet_team():
    return "Hello, Meet our team!"


@app.route("/data")
def data():
    return "IT JOB WATCH!"

# app.run(debug=True, port=8000, host='0.0.0.0')


if __name__ == "__main__":
    app.run()
