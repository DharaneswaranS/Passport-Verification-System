from flask import Flask, render_template, request, jsonify
from ai.pipeline import process_passport
from config import UPLOAD_FOLDER
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verify-passport", methods=["POST"])
def verify_passport():

    file = request.files.get("passport")
    if not file:
        return jsonify({"error":"No file"}),400

    path = os.path.join(UPLOAD_FOLDER,file.filename)
    file.save(path)

    result = process_passport(path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
