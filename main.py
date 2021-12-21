import sys, os
from ossapi import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

VERSION = "0.0.1"
global _api_


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi("osustat.ui", self)

        window = self
        sb = self.statusBar()

        _api_ = ""
        cred_verified = False

        def status(message):
            sb.showMessage(message)
            print(message)

        def dump_configuration(configuration):
            status('Saving Settings...')
            with open('osustatqt.txt', 'w+') as cfg_file:
                vals = []
                for val in configuration.values():
                    vals.append(val+'\n')
                cfg_file.writelines(vals)
            status('Settings Saved successfully...')

        def load_configuration():
            with open('osustatqt.txt', 'r') as cfg_file:
                status("Reading Configuration file...")
                lines = cfg_file.readlines()
                if len(lines) != 0:
                    for line in lines:
                        lines[lines.index(line)] = line.replace("\n", '')
                    if len(lines) == 2:
                        return lines[0], lines[1]
                    else:
                        return "", ""
                else:
                    status('Configuration is blank')
                    return "", ""

        def verify_credentials(client_id, client_secret):
            status("Verifying Credentials...")
            try:
                _api = OssapiV2(int(client_id), str(client_secret))
            except APIException:
                status("Invalid Credentials!")
                return "error"
            except ValueError:
                status("Invalid Credentials!")
                return "error"
            else:
                status("Credentials Verified")
                return _api

        def submit_api_clicked():
            client_id = window.lineEdit.text()
            client_secret = window.lineEdit_3.text()

            _api_ = verify_credentials(client_id, client_secret)
            if _api_ != "error":
                self.groupBox.setVisible(False)
                dump_configuration({"client_id": client_id, "client_secret": client_secret})

        def user_search_clicked(_api):
            if not cred_verified:
                status("API credentials not setup.")
            else:
                username_query = window.lineEdit_2.text()
                status("searching")
                username = _api.search(query=username_query).users.data[0].username
                status(f"User set to {username}")
                get_user_data(_api.search(query=username).users.data[0])

        def get_user_data(user):
            get_recent_plays(user)

        def get_recent_plays(user):
            if not cred_verified:
                status("API credentials not setup.")
            else:
                window.scrollArea2 = QScrollArea

        # Loaded
        if os.path.exists('osustatqt.txt'):
            CLIENT_ID, CLIENT_SECRET = load_configuration()
            if "" not in (CLIENT_ID, CLIENT_SECRET):
                _api_ = verify_credentials(CLIENT_ID, CLIENT_SECRET)
                if _api_ != "error":
                    self.groupBox.setVisible(False)
                    cred_verified = True

        self.pushButton_2.clicked.connect(submit_api_clicked)

        if _api_ != "error":
            cred_verified = True

        self.pushButton_5.clicked.connect(lambda: user_search_clicked(_api_))


app = QApplication(sys.argv)
main_window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedHeight(743)
widget.setFixedWidth(678)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
