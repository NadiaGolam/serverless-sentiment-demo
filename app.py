from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("textfile")
    if file and file.filename.endswith(".txt"):
        text = file.read().decode("utf-8")
        sentiment = "Positive" if "good" in text.lower() else "Neutral"
        return jsonify({"text": text, "sentiment": sentiment})
    return "Invalid file", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

