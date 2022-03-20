from flask_app import app
from flask import render_template

from flask_app.models.model import Model



@app.route('/dashboard')
def dashboard():
    return render_template('models.html', models = Model.get_all())