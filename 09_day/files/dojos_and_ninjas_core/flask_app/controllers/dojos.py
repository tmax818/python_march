from flask_app import app

from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def dojo_index():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    print(dojo)
    return render_template("show_dojo.html", dojo = dojo)