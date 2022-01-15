from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from loguru import logger
from Components.recent_activity import RecentActivityItem

from Components.css_files import scrollbar_style

class RecentActivityTab(QWidget):
    def __init__(self, mainWindow):
        super().__init__()

        self.setupUi(mainWindow)
        self.offset = 0
        self.setupConnections(mainWindow)

    def show_more_clicked(self, mainWindow):
        self.verticalLayout_2.removeWidget(self.show_more_button)
        self.offset += 20
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        # print(mainWindow.config.api)
        # exit()

        logger.info(f"offset set to: {self.offset}")
        _count = 0
        for recent_activity in mainWindow.config.api.user_recent_activity(user_id=mainWindow.config.default_user.id, limit=mainWindow.config.panel_items, offset=self.offset):
            QApplication.processEvents()
            widget = RecentActivityItem(mainWindow, recent_activity)
            self.verticalLayout_2.addWidget(widget)
            _count += 1
        
        logger.debug(f"Created {_count} RecentActivity Cards")
        self.verticalLayout_2.addWidget(self.show_more_button)
        self.show_more_button.clicked.connect(lambda: self.show_more_clicked(mainWindow))


    def setupUi(self, mainWindow):
        self.resize(778, 352)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 350))
        self.verticalLayout_2 = QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.show_more_button = QPushButton(self.scrollAreaWidgetContents)
        self.show_more_button.setText("SHOW MORE")
        
        
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

        #Add to mainMenu
        try:
            mainWindow.verticalLayout_3.addWidget(self)
        except: pass
