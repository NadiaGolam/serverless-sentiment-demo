from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Serverless Sentiment Analysis Demo"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    # Simulated analysis result
    sentiment = "Positive" if "good" in text.lower() else "Neutral"
    return jsonify({"text": text, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
