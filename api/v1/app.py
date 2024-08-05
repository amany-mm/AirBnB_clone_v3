#!/usr/bin/python3
"""
Module containing Flask API
"""
from os import getenv
from flask import Flask, make_response, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views

# Initiate the Flask app
app = Flask(__name__)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(app_views)

# HTTP access control (CORS) CORS instance allowing:
# CORS instance allowing: /* for 0.0.0.0
# [0.0.0.0](any origin is allowed)
# you can see this HTTP Response Header: < Access-Control-Allow-Origin: 0.0.0.0
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(obj):
    """Method that removes current session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Method that handles 404 status in JSON format"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host, int(port), threaded=True)
