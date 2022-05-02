from flask import Flask
from flask_bootstrap import Bootstrap5
from .config import DevConfig


web = Flask(__name__, instance_relative_config=True)

#initializing extensions
bootstrap = Bootstrap5(web)

# Set up configuration
web.config.from_object(DevConfig)
web.config.from_pyfile('config.py')

from app import views