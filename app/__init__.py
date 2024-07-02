#!/usr/bin/python3
"""
initialization defines a function to create the application
"""
from flask import Flask
from dotenv import load_dotenv
from app.config import config


load_dotenv()
def create_app(conf):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config[conf])
    from app.api.v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
