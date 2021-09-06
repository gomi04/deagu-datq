from flask import Flask
app = Flask(__name__)


@app.route("/read/<topicid>")
def read(topicid):
    return str(topicid)


@app.route("/")
def home():
    return "hi"


app.run(debug=True)
