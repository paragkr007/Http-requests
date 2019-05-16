# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:48:25 2019

@author: parag
"""

import requests
response = requests.get('http://127.0.0.1:9000/')
response.status_code #200
response.content #b'<center><h2>Welcome to file-formatter bot</h2></center>'
response.text #'<center><h2>Welcome to file-formatter bot</h2></center>'
response.url #'http://127.0.0.1:9000/'
response.encoding #'utf-8'
response.json #<bound method Response.json of <Response [200]>>
response.headers#{'Date': 'Thu, 16 May 2019 18:58:42 GMT', 'Server': 'WSGIServer/0.2 CPython/3.6.5', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Length': '55'}
response.headers['content-type'] #key - case insensitive