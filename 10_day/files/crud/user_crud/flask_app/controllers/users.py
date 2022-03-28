<<<<<<< HEAD
from flask_app import app #! importing app from __init__.py
=======
from flask_app import app  #! importing app from __init__.py
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
from flask import render_template,redirect,request,session,flash
#! these are the methods we use in routes, imported from the flask module

from flask_app.models.user import User
# ! import the models we need for the route

<<<<<<< HEAD
## READ
=======
##! READ
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
## TODO creates the root route of the app and displays all users
@app.route('/')
@app.route('/users')
def index():
<<<<<<< HEAD
    users = User.get_all() #! class method in User class, find it in ../controllers/user.py
    return render_template('index.html', users = users)

##! CREATE
=======
    users = User.get_all()  #! class method in User class, find it in ../models/user.
    return render_template('index.html', users = users)
##!CREATE
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
## TODO Show the new user form
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

## TODO handle new user form
@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
<<<<<<< HEAD
    user = User.save(request.form)  #! class method in User class, find it in ../controllers/user.py
    print(user)
    return redirect(f"/users/{user}")

##! READ
## TODO route to user show page
@app.route('/users/<int:id>')
def show_user(id):
    data = {'id':id}
    user = User.get_one(data)  #! class method in User class, find it in ../controllers/user.py
    return render_template('show_user.html', user = user)

##! UPDATE
=======
    user = User.save(request.form) #! class method in User class, find it in ../controllers/user.py
    print(user)
    return redirect(f"/users/{user}")

    
#! READ
## TODO route to user show page
@app.route('/users/<int:id>')
def show_user(id):
    data = {'id':id} #! the value of this dict has to match the id in the query string in the get_one method
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

#! UPDATE
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
## TODO route to edit user form
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)  #! class method in User class, find it in ../controllers/user.py
    return render_template('edit_user.html', user = user)

## TODO handle user edit
@app.route('/edit/user', methods=['POST'])
def update_user():
    print(request.form)
    user = User.update(request.form)  #! class method in User class, find it in ../controllers/user.py
    print(user)
    return redirect(f"/users/{request.form['id']}")

<<<<<<< HEAD
##! DELETE
## TODO route to handle delete functionality
@app.route('/delete/<int:id>')
def destroy_user(id):
    data = {'id':id}
    User.destroy(data)  #! class method in User class, find it in ../controllers/user.py
=======
#! DELETE
@app.route('/delete/<int:id>')
def destroy_user(id):
    data = {'id':id}
    User.destroy(data)   #! class method in User class, find it in ../controllers/user.py
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
    return redirect('/')
