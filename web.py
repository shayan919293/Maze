from flask import Flask, render_template
from flask import json

app = Flask(__name__)


@app.route("/")
def homepage(): 
    """ Display for / route. Displays all scores sorted in a decending format. """
    json_file = None
    with open("scores.json", "r") as file:
        json_file = json.load(file)
    json_file.sort(key = lambda i: i.get("score"),reverse=True)
    return render_template("index.html",scores=json_file,row_num = len(json_file))

if __name__ == '__main__':
    app.run(debug=True)
