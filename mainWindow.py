import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.sip import dump
from settings import SettingsWindow
from ossapi import *



class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi()
		self.show()

	API = ""

	def load_config(self):
		with open('config.osustat', 'r') as config_file:
			config = config_file.readlines()
			if len(config) > 0:
				print(config)
				return config[0].replace("\n", ""), config[1]
			else: 
				print("Config File is empty!")
				return 0, 0
	
	def dump_config(self, client_id, client_secret):
		with open('config.osustat', 'w') as config_file:
			config_file.writelines([client_id,'\n', client_secret])


	def verify_credentials(self, client_id, client_secret):
		try:
			API = OssapiV2(int(client_id), client_secret)
		except:
			self.statusBar().showMessage('Invalid Credentials.')
		else:
			self.dump_config(client_id, client_secret)
			self.statusBar().showMessage('Credentials validated. Ready')

		

	def ShowSettings(self):
		settings = SettingsWindow()
		# settings.show()
		self.horizontalLayout_2.addWidget(settings)
		client_id = settings.client_id_field.text()
		client_secret = settings.client_secret_field.text()
		settings.submit_credentials.clicked.connect(lambda: self.verify_credentials(client_id, client_secret))
		


	

	def setupUi(self):
		self.setObjectName("self")
		self.resize(744, 716)
		self.setMinimumSize(QtCore.QSize(744, 716))
		self.setMaximumSize(QtCore.QSize(744, 716))
		self.setStyleSheet("background-color: rgb(28,23,25);")
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(10, 12, 726, 80))
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.frame.sizePolicy().hasHeightForWidth())
		self.frame.setSizePolicy(sizePolicy)
		self.frame.setMinimumSize(QtCore.QSize(726, 0))
		self.frame.setMaximumSize(QtCore.QSize(726, 80))
		self.frame.setStyleSheet("""
		background-color: rgb(70,56,62);
		"border-radius: 7px;""")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.lineEdit = QtWidgets.QLineEdit(self.frame)
		self.lineEdit.setGeometry(QtCore.QRect(72, 28, 509, 31))
		font = QtGui.QFont()
		font.setFamily("Torus Pro SemiBold")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.lineEdit.setFont(font)
		self.lineEdit.setStyleSheet("color: rgb(189,170,179);")
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(44, 32, 24, 24))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/image/search.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.pushButton_4 = QtWidgets.QPushButton(self.frame)
		self.pushButton_4.setGeometry(QtCore.QRect(588, 20, 97, 41))
		self.pushButton_4.setStyleSheet("QPushButton {\n"
		"font: 63 11pt \"Torus Pro SemiBold\";\n"
		"color: white;\n"
		"border-radius: 15;\n"
		"background-color: rgb(172,57,109);\n"
		"}\n"
		"\n"
		"QPushButton:hover {\n"
		"background-color: rgb(255,102,171);\n"
		"\n"
		"}")
		self.pushButton_4.setObjectName("pushButton_4")
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(0, 160, 751, 509))
		self.frame_2.setStyleSheet("background-color: rgb(42,35,39);\n"
		"color: rgb(255,255,255)")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.frame_3 = QtWidgets.QFrame(self.centralwidget)
		self.frame_3.setGeometry(QtCore.QRect(0, 110, 751, 40))
		self.frame_3.setStyleSheet("QFrame {background-color: rgb(42,35,39);\n"
		"border-style: none;\n"
		"border-bottom-style: solid;\n"
		"border-width: 2px;\n"
		"border-bottom-color: rgb(255,102,171);\n"
		"border-top-style: none;\n"
		"color: #fff;}\n"
		"\n"
		"QPushButton {\n"
		"border: none;\n"
		"color: white;\n"
		"background-color: rgb(42,35,39);\n"
		"    font: 63 12pt \"Torus Pro SemiBold\";\n"
		"}\n"
		"\n"
		"QPushButton:hover {\n"
		"border-style: none;\n"
		"border-bottom-style: solid;\n"
		"border-width: 7px;\n"
		"border-bottom-color:  rgb(255,102,171);\n"
		"\n"
		"color: white;\n"
		"background-color:rgb(42,35,39);\n"
		"margin-top: 7px;\n"
		"    font: 63 12pt \"Torus Pro SemiBold\";\n"
		"}")
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
		self.horizontalLayout.setContentsMargins(129, 0, 129, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy)
		self.pushButton_3.setStyleSheet("")
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout.addWidget(self.pushButton_3)
		self.pushButton = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_5.setGeometry(QtCore.QRect(8, 584, 729, 41))
		self.pushButton_5.setStyleSheet("QPushButton {\n"
		"font: 63 11pt \"Torus Pro SemiBold\";\n"
		"color: white;\n"
		"border-radius: 15;\n"
		"background-color: rgb(172,57,109);\n"
		"}\n"
		"\n"
		"QPushButton:hover {\n"
		"background-color: rgb(255,102,171);\n"
		"\n"
		"}")
		self.pushButton_5.setObjectName("pushButton_5")
		self.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 62))
		self.menubar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 57, 109, 255), stop:1 rgba(255, 255, 255, 0));\n"
		"font: 63 10pt \"Torus Pro SemiBold\";\n"
		"padding: 20px;\n"
		"color: rgb(255,255,255);")
		self.menubar.setObjectName("menubar")
		self.menuPreferences = QtWidgets.QMenu(self.menubar)
		self.menuPreferences.setObjectName("menuPreferences")
		self.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setStyleSheet("background-color: rgb(42,35,39);\n"
		"font: 9pt \"Torus Pro\";\n"
		"color: rgb(255, 255, 255);")
		self.statusbar.setObjectName("statusbar")
		self.setStatusBar(self.statusbar)
		self.actionSettings = QtWidgets.QAction(self)
		self.actionSettings.setObjectName("actionSettings")
		self.menuPreferences.addAction(self.actionSettings)
		self.actionSettings.triggered.connect(self.ShowSettings)
		self.menubar.addAction(self.menuPreferences.menuAction())
		self.setWindowTitle("OsuStat Settings")
		self.lineEdit.setPlaceholderText("type to search")
		self.pushButton_4.setText("Search")
		self.pushButton_3.setText("Recent")
		self.pushButton.setText("Beatmap")
		self.pushButton_2.setText("User")
		self.pushButton_5.setText("Refresh")
		self.menuPreferences.setTitle("Preferences")
		self.actionSettings.setText("Settings")

		if os.path.exists('config.osustat'):
			self.statusBar().showMessage('Reading Config')
			client_id, client_secret = self.load_config()
			if 0 in [client_id, client_secret]:
				self.statusBar().showMessage('Credentials not found in config file. You have to manually go to settings to set it up.')
			else:
				self.verify_credentials(client_id, client_secret)


		


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
