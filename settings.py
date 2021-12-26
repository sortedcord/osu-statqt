from PyQt5 import QtCore, QtGui, QtWidgets



class SettingsWindow(QtWidgets.QWidget):
	def __init__(self, *args, **kwargs):
		super(SettingsWindow, self).__init__(*args, **kwargs)
		self.setupUi()


	def setupUi(self):
		self.resize(700, 296)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		# self.setMinimumSize(QtCore.QSize(700, 296))
		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.setStyleSheet("background-color:rgb(24,22,29);\n"
		"color: rgb(255,255,255);")
		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.frame_2 = QtWidgets.QFrame(self)
		self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
		self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
		self.frame_2.setStyleSheet("background-color: rgb(35,31,47);\n"
		"")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
		self.horizontalLayout_2.setSpacing(12)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_5 = QtWidgets.QLabel(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy)
		self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
		self.label_5.setText("")
		self.label_5.setPixmap(QtGui.QPixmap(".\\Screens\\../Assets/settings_icon.png"))
		self.label_5.setScaledContents(True)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout_2.addWidget(self.label_5)
		self.label_4 = QtWidgets.QLabel(self.frame_2)
		self.label_4.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";")
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_2.addWidget(self.label_4)
		self.verticalLayout.addWidget(self.frame_2)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(self)
		self.label.setMinimumSize(QtCore.QSize(240, 0))
		self.label.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
		"background-color:rgb(36,35,43);")
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.frame = QtWidgets.QFrame(self)
		self.frame.setStyleSheet("background-color:rgb(49,47,56);\n"
		"font: 63 12pt \"Torus Pro SemiBold\";\n"
		"color: rgb(148, 143, 163)")
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
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_id_field)
		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setObjectName("label_3")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
		self.client_secret_field = QtWidgets.QLineEdit(self.frame)
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
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.client_secret_field)
		self.submit_credentials = QtWidgets.QPushButton(self.frame)
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
		self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.submit_credentials)
		self.get_credentials = QtWidgets.QPushButton(self.frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.get_credentials.sizePolicy().hasHeightForWidth())
		self.get_credentials.setSizePolicy(sizePolicy)
		self.get_credentials.setMinimumSize(QtCore.QSize(160, 0))
		self.get_credentials.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
		"color: rgb(255, 255, 255);\n"
		"padding: 6px;\n"
		"border-radius:8px;\n"
		"text-align: center;}\n"
		"\n"
		"QPushButton:hover {    \n"
		"    background-color: rgb(140, 102, 255);\n"
		"}")
		self.get_credentials.setObjectName("get_credentials")
		self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.get_credentials)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
		self.horizontalLayout.addWidget(self.frame)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.setWindowTitle("OsuStatQt")
		self.label_4.setText("dashboard")
		self.label.setText("Credentials")
		self.label_2.setText("client id")
		self.label_3.setText("client secret")
		self.submit_credentials.setText("Submit")
		self.get_credentials.setText("Get Credentials")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SettingsWindow()
    sys.exit(app.exec_())