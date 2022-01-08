from PyQt5 import QtCore, QtWidgets

from Components.recent_activity import RecentActivityItem
from Components.recent_scores import RecentScoreItem
from Components.css_files import scrollbar_style

from loguru import logger

class RecentActivityTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.offset = 0
        self.setupConnections(mainWindow)

    def show_more_clicked(self, mainWindow):
        self.verticalLayout_2.removeWidget(self.show_more_button)
        self.offset += 20
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        logger.info(f"offset set to: {self.offset}")
        for recent_activity in mainWindow.config.api.user_recent_activity(user_id=mainWindow.default_user_class.id, limit=15, offset=self.offset):
            widget = RecentActivityItem(mainWindow, recent_activity)
            self.verticalLayout_2.addWidget(widget)
        
        self.verticalLayout_2.addWidget(self.show_more_button)
        self.show_more_button.clicked.connect(lambda: self.show_more_clicked(mainWindow))


    def setupUi(self):
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

        self.show_more_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.show_more_button.setText("SHOW MORE")
        self.show_more_button.setObjectName("show_more_button")
        
        
        self.scrollArea.setStyleSheet(scrollbar_style)
        self.setStyleSheet("""background-color: #2A2327;
                           color:rgb(255,255,255);
                           font: 63 9pt "Torus Pro"; 
                           border: none;""")

        self.show_more_button.setStyleSheet("""
            QPushButton {
                background:rgb(85,68,76);
                border:none;
                border-radius: 14px;
                padding: 7px;
                max-width:140px;
                font: 63 9pt \"Torus Pro SemiBold\";
                margin-top: 10px;

            }
            QPushButton:hover {
                background: rgb(112,92,101);
            }
        """)


class RecentScoreTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.offset = 0
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        for recent_score in mainWindow.config.api.user_scores(mainWindow.default_user_class.id, 'recent', str(int(mainWindow.config.show_failed_scores)), limit=10, offset=self.offset):
            widget = RecentScoreItem(recent_score)
            self.verticalLayout_2.addWidget(widget)
        
        self.verticalLayout_2.addWidget(self.show_more_button)
        self.show_more_button.clicked.connect(lambda: self.show_more_clicked(mainWindow))
        

        
    def show_more_clicked(self, mainWindow):
        self.verticalLayout_2.removeWidget(self.show_more_button)
        self.offset += 20
        self.setupConnections(mainWindow)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
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

        self.show_more_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.show_more_button.setText("SHOW MORE")
        self.show_more_button.setObjectName("show_more_button")

        self.setStyleSheet("""background-color: #2A2327;
                           color:rgb(255,255,255);
                           font: 63 9pt "Torus Pro"; 
                           border: none;""")

        self.show_more_button.setStyleSheet("""
            QPushButton {
                background:rgb(85,68,76);
                border:none;
                border-radius: 14px;
                padding: 7px;
                max-width:140px;
                font: 63 9pt \"Torus Pro SemiBold\";

            }
            QPushButton:hover {
                background: rgb(112,92,101);
            }
        """)
