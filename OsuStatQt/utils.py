from PyQt5.QtWidgets import QMessageBox
from ossapi import *
import datetime
# import oppai


def search_user(self, query):
    try:
        user = self.api.search(query=query).users.data[0]
    except:
        return None
    else:
        return user


def get_time_elapsed(d1):
    d2 = datetime.datetime.now(datetime.timezone.utc)
    dif = d2 - d1

    hours = (dif.seconds)//(60*60)
    minutes = (dif.seconds)//(60)

    if dif.days >= 1:
        return f"{dif.days} days ago"
    elif dif.days < 1 and hours >= 1:
        return f"{hours} hours ago"
    elif (dif.days, hours) < (1, 1) and minutes >= 1:
        return f"{minutes} minutes ago"
    elif (dif.days, hours, minutes) < (1, 1, 1):
        return f"A few seconds ago"


class MsgBox(QMessageBox):
    def __init__(self, text, icon="information"):
        super().__init__()

        if icon == "critical":
            icon = QMessageBox.Critical
        elif icon == "warning":
            icon = QMessageBox.Warning
        elif icon == "information":
            icon = QMessageBox.Information
        elif icon == "question":
            icon = QMessageBox.Question

        self.setWindowTitle("OsuStatQt")
        self.setIcon(icon)
        self.setText(text)

        _ = self.exec_()
