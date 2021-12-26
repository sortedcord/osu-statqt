from PyQt5 import QtCore, QtGui, QtWidgets


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupText(mainWindow)
        # self.show()
        self.setupStyle()
        # self.setupConnections()


    def setupUi(self):
        self.resize(800, 466) 
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(240, 0))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(50, 30, 50, -1)
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.client_id_field = QtWidgets.QLineEdit(self.frame)
        self.client_id_field.setObjectName("client_id_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_id_field)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.client_secret_field = QtWidgets.QLineEdit(self.frame)
        self.client_secret_field.setObjectName("client_secret_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.client_secret_field)
        self.submit_credentials = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Screens\\../Assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_credentials.setIcon(icon)
        self.submit_credentials.setObjectName("submit_credentials")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.submit_credentials)
        self.get_credentials = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_credentials.sizePolicy().hasHeightForWidth())
        self.get_credentials.setSizePolicy(sizePolicy)
        self.get_credentials.setMinimumSize(QtCore.QSize(160, 0))
        self.get_credentials.setObjectName("get_credentials")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.get_credentials)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)

    def setupText(self, mainWindow):
        self.setWindowTitle("Settings")
        self.label_4.setText("      settings")
        self.label.setText("Credentials")
        self.label_2.setText("client id")
        self.label_3.setText("client secret")
        self.submit_credentials.setText("Submit")
        self.get_credentials.setText("Get Credentials")

        if mainWindow.api != 0:
            self.client_id_field.setText(mainWindow.config[0])
            self.client_secret_field.setText(mainWindow.config[1])
    
    def setupStyle(self):
        self.setStyleSheet("""
            background-color:rgb(24,22,29);
            color: rgb(255,255,255);
            padding:0px;
        """)

        self.frame_2.setStyleSheet("""
            background-color: rgb(35,31,47);
        """)

        self.label.setStyleSheet("""
            font: 63 18pt \"Torus Pro SemiBold\";
            background-color:rgb(36,35,43);
            padding-left: 30px
        """)

        self.frame.setStyleSheet("""
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

        self.get_credentials.setStyleSheet("""
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
