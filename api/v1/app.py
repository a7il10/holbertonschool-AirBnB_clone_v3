#!/usr/bin/python3
"""App"""

from api.v1.views import app_views
from flask import Flask
from models import storage
import os
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(error):
    """Close storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return a JSON-formatted 404 status code response"""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
