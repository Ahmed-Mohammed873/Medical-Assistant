from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from backend.pipeline import run_pipeline

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is empty"}), 400

    result = run_pipeline(message)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)