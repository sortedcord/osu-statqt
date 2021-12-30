from PyQt5 import QtCore, QtGui, QtWidgets
from functions import OsuStatUser
import webbrowser


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupText(mainWindow)
        self.setupStylesheet()
        self.setupConnections(mainWindow)
    
    def get_credentials_clicked(self):
        webbrowser.open("https://osu.ppy.sh/home/account/edit")

    
    def reload_settings_window(self, mainWindow):
        if mainWindow.config.cred_verification_status == 'VERIFIED':
            self.frame_6.setEnabled(True)
            self.frame_8.setEnabled(True)
            self.set_default_user.setStyleSheet("""
            QPushButton {
                background-color: rgb(86,57,172);
                color: rgb(255, 255, 255);
                padding: 6px;
                border-radius:8px;
                max-width:110px;
                text-align: center;}
            
            QPushButton:hover {    
                background-color: rgb(140, 102, 255);
            }
            """)
            self.client_id_field.setText(str(mainWindow.config.client_id))
            self.client_id_field.setEnabled(False)

            self.client_secret_field.setText(mainWindow.config.client_secret)
            self.client_secret_field.setEnabled(False)

            self.default_user_field.setText(mainWindow.config.default_user)
        else:
            self.frame_6.setEnabled(False)
            self.frame_8.setEnabled(False)
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
        self.set_default_user.clicked.connect(
            lambda: self.set_default_user_clicked(mainWindow))
        
        self.load_refresh_cooldown(mainWindow)
        
        if mainWindow.default_user_class is not None:
            self.default_user_field.setText(mainWindow.default_user_class.username)
    
    def load_refresh_cooldown(self,mainWindow):
        try:
            self.refresh_limit_combo.setCurrentIndex(self.refresh_cooldown_values.index(mainWindow.config.refresh_cooldown))
        except IndexError:
            print("That value of refresh cooldown is not supported")
    
    def save_refresh_cooldown_clicked(self, mainWindow):
        if self.refresh_limit_combo.currentIndex() < 2:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("OsuStatQt")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("""
Although you can, but it is highly recommended 
not to set the refresh cooldown value below 10 
seconds as it may cause spamming of the refresh button.
            """)
            _msg = msg.exec_()
        mainWindow.config.refresh_cooldown = self.refresh_cooldown_values[self.refresh_limit_combo.currentIndex()]



    def set_default_user_clicked(self, mainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("OsuStatQt")

        if mainWindow.config.cred_verification_status == 'VERIFIED':
            x = OsuStatUser(mainWindow.config.api).search_user(
                self.default_user_field.text())
            print('User ID: ', x)

            if x == 0:  # If no user is found in Bancho
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("\
    Could not find the specified default user in bancho. \
    Kindly set the default user again in the settings.\
            ")
            else:  # If user is found
                mainWindow.default_user_class = OsuStatUser(
                    mainWindow.config.api, id=x)
                print("Default User has been set")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                mainWindow.enable_refresh_button()
                msg.setText(
                    f"Default User has been set as {mainWindow.default_user_class.username}")
        else:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(
                f"Credentials have not been setup yet. Please check your settings.")

        # Display Message Box
        _i = msg.exec_()

        #Refresh Settings Window
        self.reload_settings_window(mainWindow)


    def submit_credentials_clicked(self, mainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("OsuStatQt")

        # If not already authenticated
        if mainWindow.config.cred_verification_status != 'VERIFIED':

            mainWindow.config.client_id = self.client_id_field.text()
            mainWindow.config.client_secret = self.client_secret_field.text()
            mainWindow.config.verify_credentials()

            # If credentials are correct
            if mainWindow.config.cred_verification_status == 'VERIFIED':

                # Disable Text Fields
                self.client_id_field.setEnabled(False)
                self.client_secret_field.setEnabled(False)

                mainWindow.alert_frame.setParent(None)

                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(
                    "Authenticated Successfully, you may use this client now.")

            # If invalid credentials
            else:
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Invalid Credentials. Please Try Again.")

        # If already Authenticated
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("You are already authenticated!")
        x = msg.exec_()  # this will show our messagebox

        #Refresh Settings Window
        self.setupConnections(mainWindow)


    def setupConnections(self, mainWindow):
        # If credentials verified
        if mainWindow.config.cred_verification_status == 'VERIFIED':
            self.frame_6.setEnabled(True)
            self.frame_8.setEnabled(True)
            self.set_default_user.setStyleSheet("""
                QPushButton {
                    background-color: rgb(86,57,172);
                    color: rgb(255, 255, 255);
                    padding: 6px;
                    border-radius:8px;
                    max-width:110px;
                    text-align: center;}
                    
                QPushButton:hover {    
                    background-color: rgb(140, 102, 255);
                }
            """)
            self.client_id_field.setText(str(mainWindow.config.client_id))
            self.client_id_field.setEnabled(False)

            self.client_secret_field.setText(mainWindow.config.client_secret)
            self.client_secret_field.setEnabled(False)

            self.get_credentials_3.clicked.connect(lambda: self.get_credentials_clicked())

            if mainWindow.default_user_class is not None:
                self.default_user_field.setText(mainWindow.default_user_class.username)
            
        
        # If credentials not verified
        else:
            self.frame_6.setEnabled(False)
            self.frame_8.setEnabled(False)
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

        self.set_default_user.clicked.connect(
            lambda: self.set_default_user_clicked(mainWindow))
        
        self.refresh_cooldown_values = [0, 5000, 10000, 15000, 30000, 60000] # time in milliseconds
        self.load_refresh_cooldown(mainWindow)
        self.save_refresh_limit.clicked.connect(
            lambda: self.save_refresh_cooldown_clicked(mainWindow))


    def setupUi(self):
        self.resize(800, 439)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 49))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        
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
        
        self.label_7.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_3.setContentsMargins(50, 30, 50, -1)
        self.formLayout_3.setHorizontalSpacing(18)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.client_id_field = QtWidgets.QLineEdit(self.frame_5)
        
        self.client_id_field.setObjectName("client_id_field")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.client_id_field)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.client_secret_field = QtWidgets.QLineEdit(self.frame_5)

        self.client_secret_field.setObjectName("client_secret_field")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.client_secret_field)
        self.submit_credentials = QtWidgets.QPushButton(self.frame_5)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Screens\\../Assets/check.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_credentials.setIcon(icon)
        self.submit_credentials.setObjectName("submit_credentials")
        self.formLayout_3.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.submit_credentials)
        self.get_credentials_3 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.get_credentials_3.sizePolicy().hasHeightForWidth())
        self.get_credentials_3.setSizePolicy(sizePolicy)
        self.get_credentials_3.setMinimumSize(QtCore.QSize(160, 0))

        self.get_credentials_3.setObjectName("get_credentials_3")
        self.formLayout_3.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.get_credentials_3)
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

        self.label_10.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_4.setContentsMargins(50, 30, 50, -1)
        self.formLayout_4.setHorizontalSpacing(18)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.default_user_field = QtWidgets.QLineEdit(self.frame_7)

        self.default_user_field.setObjectName("default_user_field")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.default_user_field)
        self.set_default_user = QtWidgets.QPushButton(self.frame_7)

        self.set_default_user.setIcon(icon)
        self.set_default_user.setObjectName("set_default_user")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.set_default_user)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(798, 136))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setMinimumSize(QtCore.QSize(240, 0))
        self.label_12.setMaximumSize(QtCore.QSize(240, 16777215))
        
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout_5.setContentsMargins(35, 30, 50, -1)
        self.formLayout_5.setHorizontalSpacing(18)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.save_refresh_limit = QtWidgets.QPushButton(self.frame_9)
        
        self.save_refresh_limit.setIcon(icon)
        self.save_refresh_limit.setObjectName("save_refresh_limit")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.save_refresh_limit)
        self.refresh_limit_combo = QtWidgets.QComboBox(self.frame_9)
        
        self.refresh_limit_combo.setObjectName("refresh_limit_combo")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refresh_limit_combo)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_4.addWidget(self.frame_8)
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
        self.label_12.setText("OsuStat")
        self.label_13.setText("refresh limit")
        self.save_refresh_limit.setText("Save")
        self.refresh_limit_combo.setItemText(0, "No Limit")
        self.refresh_limit_combo.setItemText(1, "Every 5 Seconds")
        self.refresh_limit_combo.setItemText(2, "Every 10 Seconds")
        self.refresh_limit_combo.setItemText(3, "Every 15 Seconds")
        self.refresh_limit_combo.setItemText(4, "Every 30 Seconds")
        self.refresh_limit_combo.setItemText(5, "Every Minute")
    
    def setupStylesheet(self):
        self.setStyleSheet("""
            background-color:rgb(24,22,29);
            color: rgb(255,255,255);
            padding:0px;
        """)

        self.frame_2.setStyleSheet("""
            background-color: rgb(35,31,47);
        """)
        
        self.label_7.setStyleSheet("""
            font: 63 18pt \"Torus Pro SemiBold\";
            background-color:rgb(36,35,43);
            padding-left: 30px""")
        
        self.frame_5.setStyleSheet("""
            background-color:rgb(49,47,56);
            font: 63 12pt \"Torus Pro SemiBold\";
            color: rgb(148, 143, 163)
        """)
        
        self.client_id_field.setStyleSheet("""
            QLineEdit {
                background-color: rgb(61, 57, 70);
                border: none;
                padding: 6px;
                border-radius: 4px;
                color: rgb(255,255,255);
                font: 63 10pt \"Torus Pro SemiBold\";
            }
            
            QLineEdit:focus {
                border-style: solid;
                border-width: 2px;
                border-color:  rgb(148, 143, 163);
            }
        """)
        
        self.client_secret_field.setStyleSheet("""
            QLineEdit {
                background-color: rgb(61, 57, 70);
                border: none;
                padding: 6px;
                border-radius: 4px;
                color: rgb(255,255,255);
                font: 63 10pt \"Torus Pro SemiBold\";
            }
                
            QLineEdit:focus {
                border-style: solid;
                border-width: 2px;
                border-color:  rgb(148, 143, 163);
            }
        """)
                            
        self.submit_credentials.setStyleSheet("""
            QPushButton {
                background-color: rgb(86,57,172);
                color: rgb(255, 255, 255);
                padding: 6px;
                border-radius:8px;
                max-width:110px;
                text-align: center;
            }
                                              
            QPushButton:hover {    
                background-color: rgb(140, 102, 255);
            }
        """)

        self.get_credentials_3.setStyleSheet("""
            QPushButton {
                background-color: rgb(86,57,172);
                color: rgb(255, 255, 255);
                padding: 6px;
                border-radius:8px;
                text-align: center;
            }
                
            QPushButton:hover {    
                background-color: rgb(140, 102, 255);
            }
        """)

        self.label_10.setStyleSheet("""
            font: 63 18pt \"Torus Pro SemiBold\";
            background-color:rgb(36,35,43);
            padding-left: 30px
        """)
                            
        self.frame_7.setStyleSheet("""
            background-color:rgb(49,47,56);
            font: 63 12pt \"Torus Pro SemiBold\";
            color: rgb(148, 143, 163);
        """)

        self.default_user_field.setStyleSheet("""
            QLineEdit {
                background-color: rgb(61, 57, 70);
                border: none;
                padding: 6px;
                border-radius: 4px;
                color: rgb(255,255,255);
                font: 63 10pt \"Torus Pro SemiBold\";
            }
                                                
            QLineEdit:focus {
                border-style: solid;
                border-width: 2px;
                border-color:  rgb(148, 143, 163);
            }
        """)

        self.set_default_user.setStyleSheet("""
            QPushButton {
                background-color: rgb(86,57,172);
                color: rgb(255, 255, 255);
                padding: 6px;
                border-radius:8px;
                max-width:110px;
                text-align: center;}
                
            QPushButton:hover {    
                background-color: rgb(140, 102, 255);
            }
        """)

        self.label_12.setStyleSheet("""
            font: 63 18pt \"Torus Pro SemiBold\";
            background-color:rgb(36,35,43);
            padding-left: 30px""")

        self.frame_9.setStyleSheet("""
            background-color:rgb(49,47,56);
            font: 63 12pt \"Torus Pro SemiBold\";
            color: rgb(148, 143, 163)
        """)

        self.save_refresh_limit.setStyleSheet("""
            QPushButton {
                background-color: rgb(86,57,172);
                color: rgb(255, 255, 255);
                padding: 6px;
                border-radius:8px;
                max-width:110px;
                text-align: center;
            }
            
            QPushButton:hover {    
                background-color: rgb(140, 102, 255);
            }
        """)

        self.refresh_limit_combo.setStyleSheet("""
            background-color: rgb(61, 57, 70);
            border: none;
            padding: 6px;
            border-radius: 4px;
            color: rgb(255,255,255);
            font: 63 10pt \"Torus Pro SemiBold\";
        """)
                                        