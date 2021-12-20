import sys, os
from ossapi import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

VERSION = "0.0.1"

def status(statusbar, message):
    statusbar.showMessage(message)
    print(message)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("osustat.ui", self)

        window = self
        sb = self.statusBar()

        config = {
            "CLIENT_ID": "",
            "CLIENT_SECRET": "",
        }

        def verify_token():
            status(sb, "Verifying Credentials...")
            config["CLIENT_ID"] = window.lineEdit.text()
            config["CLIENT_SECRET"] = window.lineEdit_3.text()
            try:
                api = OssapiV2(int(config["CLIENT_ID"]), config["CLIENT_SECRET"])
            except:
                status(sb, "Invalid Credentials!")
            finally:
                status(sb, "Credentials Verified")
                with open("config.txt", "w+") as configfile:
                    configfile.write(config["CLIENT_ID"]+"\n"+config["CLIENT_SECRET"])
                    status(sb, "Config file dumped")
                    status(sb, "Ready!")
                    window.groupBox.setVisible(False)

        def load_config():
            if os.path.exists("config.txt"):
                status(sb, "Config File Found, now parsing.")
                with open("config.txt", "r") as config_file:
                    line_configs = config_file.readlines()
                    print(line_configs)
                    config = {
                        "CLIENT_ID": line_configs[0].replace("\n", ""),
                        "CLIENT_SECRET": line_configs[1],
                    }
                    verify_token()
                    return config

            else:
                return {
                    "CLIENT_ID": "",
                    "CLIENT_SECRET": "",
                }, False

        # Init
        config = load_config()
        self.pushButton_2.clicked.connect(verify_token)


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
