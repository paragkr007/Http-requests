# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:31:50 2019

@author: parag
"""

####################################################################### TImeout
requests.get('https://api.github.com', timeout=4)
requests.get('https://api.github.com', timeout=(1,1))#req timeout=1 and res timeout =1

############################################################# Timeout exception
import requests
from requests.exceptions import Timeout

try:
    res = requests.get('https://api.github.com', timeout=(2,2))    
except Timeout:
    print('The request timed out!')
else:
    print('Req didn\'t timed out')


####################################################################### Session
'''
 Sessions : to improve performance
 Same authnetication can be used for multiple requests.
'''
import requests
from getpass import getpass

with requests.Session() as session:
    session.auth = ('username',getpass())
    response = session.get('https://api.github.com/user')

print(response.headers)
print(reponse.json())


################################################################### Max_Retries
'''
Max_Retries : when you want to try same request multiple times.
Need to implement a custom Transport Adapter
'''
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)
session = requests.Session()

session.mount('https://api.githubw.com',github_adapter)

try:
    r = session.get('https://api.githubw.com')
    print(r.json())
except ConnectionError as e:
    print(e)
    

##################### Max_retries with Back off(sleep before retrying) strategy
import requests
from urllib3.util.retry import Retry    
from requests.adapters import HTTPAdapter

sess = requests.Session()
retries = Retry(total =5,
                backoff_factor=0.1,
                status_forcelist=[500,502,503,504,505])

sess.mount('http://',HTTPAdapter(max_retries=retries))

sess.get('http://httpstat.us/500')
