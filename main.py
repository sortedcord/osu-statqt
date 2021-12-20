import sys, os
from ossapi import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

VERSION = "0.0.1"





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("osustat.ui", self)

        window = self
        sb = self.statusBar()

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
                if len(lines)!= 0:
                    lines[0] = lines[0].replace('\n', '')
                    lines[1] = lines[1].replace('\n', '')
                    print(lines)
                    #11627
                    #jfkuMglKmdsM58wMnlzAwwLrmps5A1qwhVCskDKn
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
                _api = OssapiV2(int(client_id), client_secret)
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

            _api = verify_credentials(client_id, client_secret)
            if _api != "error":
                self.groupBox.setVisible(False)
                dump_configuration({"client_id": client_id, "client_secret": client_secret})
            return _api

        # Loaded
        if os.path.exists('osustatqt.txt'):
            CLIENT_ID, CLIENT_SECRET = load_configuration()
            if "" not in (CLIENT_ID, CLIENT_SECRET):
                api = verify_credentials(CLIENT_ID, CLIENT_SECRET)
                if api != "error":
                    self.groupBox.setVisible(False)

        self.pushButton_2.clicked.connect(submit_api_clicked)


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
