import os
from ossapi import *

def load_config():
    if os.path.exists('config.osustat'):
        print("Config File Found")
        with open('config.osustat', 'r') as config_file:
            configs = []
            configfile = config_file.readlines()
            if len(configfile) > 0:
                for config in configfile:
                    configs.append(config.replace('\n', ''))
                print(configs)
                return configs
            else: return 0
    else: return 0

def verify_credentials(client_id, client_secret):
    try:
        api = OssapiV2(client_id, client_secret)
    except:
        api = 0
    else:
        return api
