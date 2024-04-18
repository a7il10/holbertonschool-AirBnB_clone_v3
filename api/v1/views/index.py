#!/usr/bin/python3
"""Index module"""


from flask import jsonify, Flask
from api.v1.views import app_views
from models import storage


app = Flask(__name__)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns a JSON response"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def counter():
    """Retrieves the number of each objects by type"""
    classes = {"Amenity": "amenities", "City": "cities",
               "Place": "places", "Review": "reviews",
               "State": "states", "User": "users"}
    count = {}
    for key, value in classes.items():
        count[value] = storage.count(key)
    return jsonify(count)
