
import os
from ossapi import OssapiV2
from ossapi import *
import oauthlib
import requests


class Config():
    def __init__(self, client_id=None, client_secret=None, default_user=None):

        self.client_id = client_id
        self.client_secret = client_secret
        self.cred_verification_status = 'UNVERIFIED'
        self.default_user = default_user
        self.api = None

        if None not in (self.client_id, self.client_secret):
            self.verify_credentials()

    def load_config(self):
        if os.path.exists('config.osustat'):
            with open('config.osustat', 'r') as f:
                raw_configs = f.readlines()
                formatted_config = {}
                for config in raw_configs:
                    key, value = config.replace('\n', '').split(' : ')
                    if value == '0':
                        value = None
                    formatted_config[key] = value

            self.client_id = formatted_config['client_id']
            self.client_secret = formatted_config['client_secret']
            self.default_user = formatted_config['default_user']
            self.verify_credentials()

    def dump_config(self):
        with open('config.osustat', 'w') as w:

            for index in range(len(self.__dict__.keys())):

                key = list(self.__dict__.keys())[index]
                value = list(self.__dict__.values())[index]

                if value is None:
                    w.write(f"{key} : {0}")
                else:
                    w.write(f"{key} : {value}")
                w.write("\n")

    def verify_credentials(self):
        print('Credentials:', self.client_id, self.client_secret)

        if None in (self.client_id, self.client_secret):
            self.cred_verification_status = 'UNVERIFIED'

        else:
            # Putting this in a different try block to save time
            if 'str' in str(type(self.client_id)):
                try:
                    self.client_id = int(self.client_id)
                except ValueError:
                    self.cred_verification_status = 'INVALID'

            try:
                self.api = OssapiV2(self.client_id, self.client_secret)
            except oauthlib.oauth2.rfc6749.errors.InvalidClientError:
                self.cred_verification_status = 'INVALID'
            except requests.exceptions.ConnectionError:
                self.cred_verification_status = 'NO_INTERNET'
            except requests.exceptions.ConnectionError:
                self.cred_verification_status = 'NO_INTERNET'
            else:
                self.cred_verification_status = 'VERIFIED'
