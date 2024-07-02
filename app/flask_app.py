#!/usr/bin/python3
from os import getenv
from app import create_app

app = create_app(getenv('CONFIG') or 'default')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)
