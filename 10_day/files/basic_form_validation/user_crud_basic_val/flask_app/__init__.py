# __init__.py

#! you can keep all imports here, 
#! flash is a method we will use in the validation process
from flask import Flask, flash
import re

app = Flask(__name__)

### ! We need this for session/flash
app.secret_key = "shhhhhh"