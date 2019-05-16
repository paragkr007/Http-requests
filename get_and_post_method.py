# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:51:57 2019

@author: PA389009
"""

import json
import requests
response = requests.get('https://api.github.com/search/issues',
                        params = {'q':'topic:windows'},
                        headers={'Accept': 'application/vnd.github.v3.text-match+json'},) 
#<Response [200]>

json_res = response.json()
#json

print(response.headers)
#header details

res = requests.post('https://httpbin.org/post',json={'key':'value'})

res.request.body    
##prepared request

data =res.json()
#json
data_dict = data['data']
#json_parse
