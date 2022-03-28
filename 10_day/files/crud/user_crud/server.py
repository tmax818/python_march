from flask_app import app # ! this comes from flask_app/__init__.py
from flask_app.controllers import users # ! this comes from flask_app/controllers/users.py
#! server.py used to hold our routes, now they're in flask_app/controllers/users.py 

#! this starts our app
if __name__ == "__main__":
    app.run(debug=True)
#! call the run method on app, which is an instance of(i.e. object) our Flask class
