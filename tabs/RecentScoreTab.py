from PyQt5 import QtCore, QtWidgets

from Components.recent_scores import RecentScoreItem
from Components.css_files import scrollbar_style

from loguru import logger




class RecentScoreTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.offset = 0
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        _count = 0
        for recent_score in mainWindow.config.api.user_scores(mainWindow.default_user_class.id, 'recent', str(int(mainWindow.config.show_failed_scores)), limit=mainWindow.config.panel_items, offset=self.offset):
            QtWidgets.QApplication.processEvents()
            widget = RecentScoreItem(mainWindow, recent_score)
            self.verticalLayout_2.addWidget(widget)
            _count += 1
        
        logger.debug(f"Created {_count} RecentScoreItem cards")
        self.verticalLayout_2.addWidget(self.show_more_button)
        self.show_more_button.clicked.connect(lambda: self.show_more_clicked(mainWindow))
        

        
    def show_more_clicked(self, mainWindow):
        self.verticalLayout_2.removeWidget(self.show_more_button)
        self.offset += 20
        self.setupConnections(mainWindow)

    def setupUi(self, mainWindow):
        self.resize(778, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 350))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea.setStyleSheet(scrollbar_style)

        self.show_more_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.show_more_button.setText("SHOW MORE")

        self.setStyleSheet("""
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

        try:
            mainWindow.verticalLayout_4.addWidget(self)
        except: pass
