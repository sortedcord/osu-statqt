import os
from ossapi import *
from PyQt5 import QtCore, QtWidgets

class OsuStatUser():
    """ IN CASE YOU ARE NOT USING THIS CLASS TO SEARCH FOR USERS:
    Never initialize an object of this class with both the user and id 
    as none as it will not work. One of the arguments needs to have the 
    correct value.
    """

    def __init__(self, api, username= None, id= None):
        self.username = username
        self.id = id
        self.api = api
        
        if self.username is not None and self.id is None:
            self.id = self.search_user(self.username)
        elif self.id is not None:
            self.username = self.api.user(self.id).username


    def search_user(self, query):
        try:
            user = self.api.search(query=query).users.data[0]
        except: return 0
        else: 
            return user.id


def load_config():
    if os.path.exists('config.osustat'):
        with open('config.osustat', 'r') as config_file:
            configs = []
            configfile = config_file.readlines()
            if len(configfile) > 0:
                for config in configfile:
                    configs.append(config.replace('\n', ''))
                return configs
            else:
                return []
    else:
        return []


def verify_credentials(client_id, client_secret):
    try:
        api = OssapiV2(client_id, client_secret)
    except:
        api = 0
        return api
    else:
        return api


def dump_config(configs):
    with open('config.osustat', 'w') as config_file:
        for config in configs:
            config_file.write(config+'\n')

    