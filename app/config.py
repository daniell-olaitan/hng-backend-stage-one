#!/usr/bin/python3
"""
module defines the configuration of the application
"""
from os import getenv


class Config:
    WEATHER_API_KEY = getenv('WEATHER_API_KEY')


class DevConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'default': Config,
    'dev': DevConfig,
    'production': ProductionConfig
}
