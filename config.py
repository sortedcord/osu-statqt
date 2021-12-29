import pickle as pkl
import os
from ossapi import OssapiV2
from ossapi import *
import oauthlib
import requests


class Config:
    def __init__(self, client_id=None, client_secret=None, default_user=None):

        self.client_id = client_id
        self.client_secret = client_secret
        self.cred_verification_status = "UNVERIFIED"
        self.default_user = default_user
        self.api = None

    def dump_config(self):
        with open("config.osustat", "wb") as w:
            self.api = None
            pkl.dump(self, w)

    def verify_credentials(self):
        print("Credentials:", self.client_id, self.client_secret)

        if None in (self.client_id, self.client_secret):
            self.cred_verification_status = "UNVERIFIED"

        else:
            # Putting this in a different try block to save time
            if "str" in str(type(self.client_id)):
                try:
                    self.client_id = int(self.client_id)
                except ValueError:
                    self.cred_verification_status = "INVALID"

            try:
                self.api = OssapiV2(self.client_id, self.client_secret)
            except oauthlib.oauth2.rfc6749.errors.InvalidClientError:
                self.cred_verification_status = "INVALID"
            except requests.exceptions.ConnectionError:
                self.cred_verification_status = "NO_INTERNET"
            except requests.exceptions.ConnectionError:
                self.cred_verification_status = "NO_INTERNET"
            else:
                self.cred_verification_status = "VERIFIED"


def load_config():
    if os.path.exists("config.osustat"):
        try:
            with open("config.osustat", "rb") as f:
                config = pkl.load(f)
                print(
                    f"=========== CONFIG LOADED =========== \n",
                    f"Client ID: {config.client_id} \n"
                    f"Default User: {config.default_user} \n",
                )
                config.verify_credentials()
                return config
        except EOFError:
            print("The config is empty.")
            return Config()
        except pkl._pickle.UnpicklingError:
            print("The config is corrupted.")

    else:
        print("Config not found")
        return Config()
