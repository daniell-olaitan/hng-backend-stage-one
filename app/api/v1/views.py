#!/usr/bin/python3
"""
module implements the api endpoint of the application
"""
from flask import request, jsonify
from . import api
from app.helpers import get_location_and_weather


@api.route('/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.headers.get('X-Real-IP') or request.remote_addr
    resp = get_location_and_weather(client_ip)
    if resp:
        city, temperature = resp

        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
        resp = {
            "client_ip": client_ip,
            "location": city,
            "greeting": greeting,
        }
        return jsonify(resp)

    return jsonify({'error': 'Network Error'})
