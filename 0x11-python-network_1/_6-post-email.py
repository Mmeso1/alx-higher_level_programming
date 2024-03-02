#!/usr/bin/python3
""" POST an email """

import requests
from sys import argv

from flask import Flask, request

app = Flask(__name__)

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    print(f'Your email is: {email}')
    return 'Email received successfully'

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

