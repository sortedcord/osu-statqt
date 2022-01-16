import sys, webbrowser
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from Components.controls import CustomLabel
from Components.layouts import CustomSizePolicy
from utils import MsgBox

from loguru import logger

from version import __version__

class AboutWindow(QWidget):
	def __init__(self, mainWindow):
		super().__init__()

		self.resize(550, 215)
		self.setMinimumSize(QtCore.QSize(550, 215))
		self.setMaximumSize(QtCore.QSize(550, 215))

		self.icon = CustomLabel(self, maxSize=(200,200), image_url=f"{mainWindow.assetpath}/Logo/logo1x.png")
		self.icon.setGeometry(QtCore.QRect(0, 10, 200, 200))
		sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred, self.icon)
		self.icon.setAlignment(QtCore.Qt.AlignCenter)

		self.title = CustomLabel(self, "OsuStatQt", 'rgb(39, 39, 39)', 37, 'Bold')
		self.title.setGeometry(QtCore.QRect(220, 30, 281, 51))
		sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.title)

		self.version = CustomLabel(self, f"Version {__version__}", "rgb(39, 39, 39)", 12, '')
		self.version.setGeometry(QtCore.QRect(220, 80, 181, 31))
		sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.version)

		self.update_check = QPushButton(self)
		self.update_check.setGeometry(QtCore.QRect(220, 150, 111, 23))
		self.update_check.clicked.connect(self.check_updates_clicked)

		self.view_repository = QPushButton(self)
		self.view_repository.setGeometry(QtCore.QRect(340, 150, 111, 23))
		self.view_repository.clicked.connect(self.view_repository_clicked)

		self.view_repository.setStyleSheet("border-style: solid;border-color: gray;border-width:1px;border-radius: 5px;")
		self.update_check.setStyleSheet("border-style: solid;border-color: gray;border-width:1px;border-radius: 5px;")
		self.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.setWindowTitle("About | OsuStat")
		self.update_check.setText("Check for Updates")
		self.view_repository.setText("View Repository")

		self.show()

	def view_repository_clicked(self):
		logger.info("View Repository button click event performed")
		webbrowser.open("https://github.com/sortedcord/osu-statqt")
		logger.info("Opening Link in Browser")
	
	def check_updates_clicked(self):
		MsgBox("Not Implemented yet. Either update or check the repository for more inofrmation")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = AboutWindow()
	sys.exit(app.exec_())
