from ossapi import *
import datetime
# import oppai
import pyttanko

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


def get_time_elapsed(d1):
    d2 = datetime.datetime.now(datetime.timezone.utc)
    dif = d2 - d1

    hours = (dif.seconds)//(60*60)
    minutes = (dif.seconds)//(60)

    if dif.days >= 1:
        return f"{dif.days} days ago"
    elif dif.days < 1 and hours >= 1:
        return f"{hours} hours ago"
    elif (dif.days,hours) < (1,1) and minutes >= 1:
        return f"{minutes} minutes ago"
    elif (dif.days,hours,minutes) < (1,1,1):
        return f"A few seconds ago"
