import logging
import os

from flask import Flask, jsonify


APP_NAME = os.getenv(
    "APP_NAME",
    "Secure Software Supply Chain Demo API"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

PORT = int(os.getenv("PORT", "5000"))


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)
app = Flask(__name__)


# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "version": APP_VERSION
    })


if __name__ == "__main__":
    logger.info("%s starting on port %s", APP_NAME, PORT)

    app.run(
        host="127.0.0.1",
        port=PORT
    )