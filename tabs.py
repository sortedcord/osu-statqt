from PyQt5 import QtCore, QtWidgets
from ossapi import enums

from Components.recent_activity import RecentActivityItem
from Components.recent_scores import RecentScoreItem
from Components.css_files import scrollbar_style

import ossapi

class RecentActivityTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        for recent_activity in mainWindow.config.api.user_recent_activity(user_id=mainWindow.default_user_class.id, limit=20, offset=0):
            widget = RecentActivityItem(mainWindow, recent_activity)
            self.verticalLayout_2.addWidget(widget)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 350))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.scrollArea.setStyleSheet(scrollbar_style)
        self.setStyleSheet("""background-color: #2A2327;
                           color:rgb(255,255,255);
                           font: 63 9pt "Torus Pro"; 
                           border: none;""")


class RecentScoreTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        for recent_score in mainWindow.config.api.user_scores(mainWindow.default_user_class.id, 'recent', "1", limit=10, offset=0):
            widget = RecentScoreItem(recent_score)
            self.verticalLayout_2.addWidget(widget)


    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
        self.setStyleSheet("background-color: #2A2327;\n"
                           "color:rgb(255,255,255);\n"
                           "font: 63 9pt \"Torus Pro SemiBold\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 350))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea.setStyleSheet(scrollbar_style)
