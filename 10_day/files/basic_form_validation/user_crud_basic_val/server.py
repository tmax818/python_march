from flask_app import app #! this comes from __init__.py
from flask_app.controllers import users


if __name__ == "__main__":
    app.run(debug=True)