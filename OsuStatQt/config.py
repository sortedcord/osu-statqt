import pickle as pkl
import os
from ossapi import OssapiV2
from ossapi import *
import oauthlib
import requests
from loguru import logger

class Config:
    def __init__(self, client_id=None, client_secret=None, default_user=None):

        self.client_id = client_id
        self.client_secret = client_secret

        self.cred_verification_status = "UNVERIFIED"
        self.api = None
        self.default_user = None


        # OsuStat Specific
        self.refresh_cooldown = 15000

        # Panels
        self.show_failed_scores = True
        self.panel_items = 15

        logger.debug(f"Config Object Defaults set.")

    def dump_config(self):
        with open("config.osustat", "wb") as w:
            _api = self.api
            self.api = None
            self.default_user._api = None

            try: 
                pkl.dump(self, w)
            except:
                logger.error("Could not dump pickled object")
            else:
                logger.info("Config Dumped successfully.")
                self.api = _api

    def verify_credentials(self):
        logger.debug(f"Verifying Credentials {self.client_id}; {self.client_secret}")

        if None in (self.client_id, self.client_secret):
            logger.error("Either of the credentials are missing. Cannot verify None Values")
            self.cred_verification_status = "UNVERIFIED"
            logger.info(f"Credentials Verification status updated to {self.cred_verification_status} ")

        else:
            logger.warning("Client ID type is string. Converting to Base10 Int")
            if "str" in str(type(self.client_id)):
                try:
                    self.client_id = int(self.client_id)
                except ValueError:
                    logger.error("Client ID contains alphanumeric characters while only integer was expected.")
                    self.cred_verification_status = "INVALID"
                    logger.info(f"Credentials Verification status updated to {self.cred_verification_status} ")
                else:
                    logger.success("Converted to Base10")

            try:
                self.api = OssapiV2(self.client_id, self.client_secret)
            except oauthlib.oauth2.rfc6749.errors.InvalidClientError:
                self.cred_verification_status = "INVALID"
                logger.error("Entered credentials are invalid.")
            except requests.exceptions.ConnectionError:
                self.cred_verification_status = "NO_INTERNET"
                logger.error("Cannot send request. Please check your network connectivity.")
            else:
                self.cred_verification_status = "VERIFIED"
                logger.success("Credentials Verified Successfully")
            logger.info(f"Credentials Verification status updated to {self.cred_verification_status} ")


def load_config():
    if os.path.exists("config.osustat"):
        logger.info("Config file found in the directory.")
        with open("config.osustat", "rb") as f:
            logger.info("Reading Config File")
            try:
                    config = pkl.load(f)
            except EOFError:
                logger.warning("Config File is Blank!")
                return Config()
            except pkl._pickle.UnpicklingError:
                logger.error("The config file is corrupted.")
            else:
                logger.success("Configurations loaded successfully")
                logger.debug("Verifying Credentials")
                config.verify_credentials()
                return config


    else:
        logger.error("Config file not found")
        return Config()

def del_config_file():
    if os.path.exists("config.osustat"):
        logger.info("Config File Found")
        try:
            os.remove("config.osustat")
        except:
            logger.error("Could not delete File")
        else:
            logger.success("Deleted config file succesfully.")