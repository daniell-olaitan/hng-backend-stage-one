#!/usr/bin/python3
"""
module implement helper functions for the application
"""
import requests
from os import getenv


def get_location_and_weather(ip):
    try:
        ip_api_url = f"http://ip-api.com/json/{ip}"
        location_response = requests.get(ip_api_url).json()
        city = location_response.get('city', 'Unknown')
        lat = location_response.get('lat')
        lon = location_response.get('lon')

        weather_api_querystring = {"q":f"{lat},{lon}"}
        weather_api_headers = {
        	"x-rapidapi-key": getenv('WEATHER_API_KEY'),
        	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
        }

        weather_api_url = "https://weatherapi-com.p.rapidapi.com/current.json"
        weather_response = requests.get(weather_api_url,
                                        headers=weather_api_headers,
                                        params=weather_api_querystring).json()
        temperature = weather_response['current'].get('temp_c', 'Unknown') if 'current' in weather_response else 'Unknown'
    except:
        return False

    return city, temperature
