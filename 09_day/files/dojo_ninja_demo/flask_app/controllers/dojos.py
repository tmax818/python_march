from flask import render_template,redirect,request,session
from flask_app import app

from flask_app.models.dojo import Dojo
@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)