# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:05:52 2019

@author: PA389009
"""
######################################################### default auhentication
from getpass import getpass

resp=requests.get('https://api.github.com/user',auth=('username',getpass()))

json_resp = resp.json()
#json with user details




######################################################### Custom authentication
import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))


########################### SSL (Secure socket layer)  Certificate Verification
'''
    SSL creates an encrypted connection between client and server.
    SSl certificate of target is checked here
'''
requests.get('https://api.github.com', verify=False)