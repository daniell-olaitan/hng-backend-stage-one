#!/usr/bin/python3
"""
module creates and initializes api blueprint
"""
from flask import Blueprint
api = Blueprint('api', __name__)

from .views import *
