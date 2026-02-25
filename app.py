from flask import Flask, jsonify
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask Microservice 🚀"
    })

@app.route("/time")
def get_time():
    return jsonify({
        "current_time": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "dev"),
        "version": os.getenv("VERSION", "v1")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)