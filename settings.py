from PyQt5 import QtCore, QtGui, QtWidgets
from functions import dump_config, OsuStatUser, verify_credentials


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupText(mainWindow)
        self.setupConnections(mainWindow)
    
    def set_default_user_clicked(self, mainWindow):
        x = OsuStatUser(mainWindow.api).search_user(self.default_user_field.text())
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("OsuStatQt")
        if x == 0: 
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("\
Could not find the specified default user in bancho. \
Kindly set the default user again in the settings.\
        ")
        else: 
            mainWindow.default_user = OsuStatUser(mainWindow.api, id=x)
            mainWindow.config[2] = (mainWindow.default_user.username)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(f"Default User has been set as {mainWindow.default_user.username}")
        x = msg.exec_()  # this will show our messagebox
        


    def submit_credentials_clicked(self, mainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("OsuStatQt")
        if mainWindow.api == 0:
            mainWindow.api = verify_credentials(
                self.client_id_field.text(), self.client_secret_field.text())
            if mainWindow.api != 0:
                self.client_id_field.setEnabled(False)
                self.client_secret_field.setEnabled(False)
                mainWindow.config[0] = self.client_id_field.text()
                mainWindow.config[1] = self.client_secret_field.text()
                mainWindow.verticalLayout.removeWidget(self.alert_frame)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(
                    "Authenticated Successfully, you may use this client now.")
            else:
                msg.setIcon(QtWidgets.QMessageBox.Critical)
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("You are already authenticated!")
        x = msg.exec_()  # this will show our messagebox

    def setupConnections(self, mainWindow):
        if mainWindow.api != 0:
            self.client_id_field.setText(mainWindow.config[0])
            self.client_id_field.setEnabled(False)
            self.client_secret_field.setText(mainWindow.config[1])
            self.client_secret_field.setEnabled(False)
            self.default_user_field.setText(mainWindow.config[2])
        else: 
            self.frame_6.setEnabled(False)
            self.set_default_user.setStyleSheet("""
            QPushButton {
                background-color: rgb(60,57,71);
                color: rgb(200, 200, 200);
                padding: 6px;
                border-radius:8px;
                max-width:110px;
                text-align: center;
            }
            """)
        self.submit_credentials.clicked.connect(
            lambda: self.submit_credentials_clicked(mainWindow))
        self.set_default_user.clicked.connect(lambda: self.set_default_user_clicked(mainWindow))


    def setupUi(self):
        self.resize(800, 439)
        self.setStyleSheet("background-color:rgb(24,22,29);\n"
"color: rgb(255,255,255);\n"
"padding:0px;")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 49))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(35,31,47);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(798, 249))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(240, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
"background-color:rgb(36,35,43);\n"
"padding-left: 30px")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setStyleSheet("background-color:rgb(49,47,56);\n"
"font: 63 12pt \"Torus Pro SemiBold\";\n"
"color: rgb(148, 143, 163)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_3.setContentsMargins(50, 30, 50, -1)
        self.formLayout_3.setHorizontalSpacing(18)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.client_id_field = QtWidgets.QLineEdit(self.frame_5)
        self.client_id_field.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.client_id_field.setObjectName("client_id_field")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_id_field)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.client_secret_field = QtWidgets.QLineEdit(self.frame_5)
        self.client_secret_field.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.client_secret_field.setObjectName("client_secret_field")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.client_secret_field)
        self.submit_credentials = QtWidgets.QPushButton(self.frame_5)
        self.submit_credentials.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"max-width:110px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Screens\\../Assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_credentials.setIcon(icon)
        self.submit_credentials.setObjectName("submit_credentials")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.submit_credentials)
        self.get_credentials_3 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_credentials_3.sizePolicy().hasHeightForWidth())
        self.get_credentials_3.setSizePolicy(sizePolicy)
        self.get_credentials_3.setMinimumSize(QtCore.QSize(160, 0))
        self.get_credentials_3.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}")
        self.get_credentials_3.setObjectName("get_credentials_3")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.get_credentials_3)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMinimumSize(QtCore.QSize(798, 136))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setMinimumSize(QtCore.QSize(240, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_10.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
"background-color:rgb(36,35,43);\n"
"padding-left: 30px")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setStyleSheet("background-color:rgb(49,47,56);\n"
"font: 63 12pt \"Torus Pro SemiBold\";\n"
"color: rgb(148, 143, 163)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_4.setContentsMargins(50, 30, 50, -1)
        self.formLayout_4.setHorizontalSpacing(18)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.default_user_field = QtWidgets.QLineEdit(self.frame_7)
        self.default_user_field.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.default_user_field.setObjectName("default_user_field")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_user_field)
        self.set_default_user = QtWidgets.QPushButton(self.frame_7)
        self.set_default_user.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"max-width:110px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}\n"
"")
        self.set_default_user.setIcon(icon)
        self.set_default_user.setObjectName("set_default_user")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.set_default_user)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.setCentralWidget(self.centralwidget)

    def setupText(self, mainWindow):
        self.setWindowTitle("MainWindow")
        self.label_4.setText("      settings")
        self.label_7.setText("Credentials")
        self.label_8.setText("client id")
        self.label_9.setText("client secret")
        self.submit_credentials.setText("Submit")
        self.get_credentials_3.setText("Get Credentials")
        self.label_10.setText("User")
        self.label_11.setText("username")
        self.set_default_user.setText("Enter")
        
