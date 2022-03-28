from flask_app import app
from flask import jsonify

from flask_app.models.model import Model

@app.route('/get_data')
def get_data():
    return jsonify(Model.data())
