# __init__.py

from flask import Flask, flash
import re

app = Flask(__name__)

### ! We need this for session/flash
app.secret_key = "shhhhhh"