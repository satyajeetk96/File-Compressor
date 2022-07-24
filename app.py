from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET", "POST"])
def home():
  return render_template("index.html")