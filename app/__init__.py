from flask import Flask
from app.config import Config

"""
Initialize the Flask application
"""
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config.from_object(Config)

from app import view
