import os
from ossapi import *
from PyQt5 import QtCore, QtWidgets


class OsuStatUser():
    """ IN CASE YOU ARE NOT USING THIS CLASS TO SEARCH FOR USERS:
    Never initialize an object of this class with both the user and id 
    as none as it will not work. One of the arguments needs to have the 
    correct value.
    """

    def __init__(self, api, username=None, id=None):
        self.username = username
        self.id = id
        self.api = api

        # Case1: Username is known and id isn't
        if self.username is not None and self.id is None:
            self.id = self.search_user(self.username)

        # Case2: Username isn't known and id is
        elif self.id is not None:
            self.username = self.api.user(self.id).username

    def search_user(self, query):
        # TODO: I'm not really sure which specific exception it raises.
        try:
            user = self.api.search(query=query).users.data[0]
        except:
            return 0
        else:
            return user.id


# TODO: Create a separate config wrapper
def load_config():

    # If the config file is found in the same directory.
    # Whenever there is something wrong with the config file,
    # it just returns an empty list.

    if os.path.exists('config.osustat'):
        with open('config.osustat', 'r') as config_file:
            # Turns out .readlines function can only be used once.
            # TODO: Convert Config List to Dictionary
            configs = []
            configfile = config_file.readlines()

            # If configfile list is not empty
            if len(configfile) > 0:
                for config in configfile:
                    configs.append(config.replace('\n', ''))
                return configs
            else:
                return []
    # If file not found.
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
            # Separate configs to new lines
            config_file.write(config+'\n')
