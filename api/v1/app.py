#!/usr/bin/python3
"""
Module containing Flask API
"""
from os import getenv
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(obj):
    """Method that removes current session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Method that handles 404 status in JSON fromat"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host, int(port), threaded=True)
