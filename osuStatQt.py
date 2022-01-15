VERSION = '0.0.5'

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

# import os
from loguru import logger
from Components.utility import CustomHLayout, CustomLabel, CustomVLayout

from config import load_config

from settings import SettingsWindow
from pathlib import Path

from tabs.RecentActivityTab import RecentActivityTab
from tabs.RecentScoreTab import RecentScoreTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  

        self.assetpath = Path(__file__).parent / "Assets"

        self.setupUi()
        self.setupText()
        logger.debug("Loaded Window UI Structure")
        self.setupStyle()
        logger.debug("Applied Stylesheet to Qt")
        self.show()
        self.setupConnections()
        logger.debug("Connections have been setup.")


    def load_tab_content(self):
        # Show Recent Activity Tab
        self.recent_activity_tab_content = RecentActivityTab(self)
    
        logger.debug("Displayed Recent Activity Tab")

        # Show Recent Scores Tab
        self.recent_scores_tab_content = RecentScoreTab(self)
        logger.debug("Displayed Recent Scores Tab")
        
        self.statusbar.showMessage("Data Refreshed")

        # Show User Tab
        # self.user_tab_content = UserTab(self)
        # self.verticalLayout_5.addWidget(self.user_tab_content)


    def refresh(self):
        logger.info("Refresh Button was clicked.")
        self.disable_refresh_button()
        logger.debug("Refresh Button disabled")   

        self.statusbar.showMessage("Refreshing... Please Wait")
        try:
            self.verticalLayout_4.removeWidget(self.recent_scores_tab_content)
            self.verticalLayout_3.removeWidget(self.recent_activity_tab_content)
            self.recent_scores_tab_content.setParent(None)
            self.recent_activity_tab_content.setParent(None)
            logger.debug("Removed Tab Contents")
        except:
            pass

        self.load_tab_content()
        self.refresh_obj = QtCore.QTimer()
        if not self.config.refresh_cooldown == 0:
            self.refresh_obj.setInterval(self.config.refresh_cooldown)
            logger.info(f"Refresh Cooldown set to {self.config.refresh_cooldown/1000} seconds")
        else:
            logger.warning("Refresh Cooldown has been disabled")
            logger.info("Setting Time Interval to 100ms to prevent GUI Freeze")
            self.refresh_obj.setInterval(100)

        self.refresh_obj.setSingleShot(True)
        self.refresh_obj.timeout.connect(self.enable_refresh_button)
        self.refresh_obj.start()
        logger.info("Started Timer")

    def enable_refresh_button(self):
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #AC396D;
                border:none;
                border-radius: 7px;
                font: 63 12pt \"Torus Pro SemiBold\";
                padding: 10px;
                min-width:80px;
            }

            QPushButton:hover {
                background-color: #FF66AB;

            }
                    """)
        self.refresh_button.clicked.connect(self.refresh)
        self.refresh_button.setEnabled(True)
    

    def disable_refresh_button(self):
        self.refresh_button.setEnabled(False)
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(122, 86, 103);
                color: rgb(200, 200, 200);
                border:none;
                border-radius: 7px;
                font: 63 12pt \"Torus Pro SemiBold\";
                padding: 10px;
                min-width:80px
            }
        """)


    def showSettings(self):
        self.settingsWindow = SettingsWindow(self)
        logger.debug("Created SettingsWindow Class Instance")
        self.settingsWindow.show()
        logger.info("Showing Settings Window")

    def setupConnections(self):
        self.actionSettings.triggered.connect(self.showSettings)  # Settings Menu
        logger.debug("Connected settings menu to 'showSettings'")

        self.config = load_config()
        logger.debug("Config Loaded")

        self.default_user_expand = None

        # If credentials were valid
        if self.config.cred_verification_status == 'VERIFIED':
            
            self.statusbar.showMessage("Credentials verified")
            logger.info("Credentials Verified")

            self.alert_frame.setParent(None)  # Remove alert frame
            logger.debug("Alert Frame Removed")

            # If config has default user set
            if self.config.default_user is not None:
                    # self.default_user_expand = self.config.default_user.expand()
                    # logger.debug("Expanded Default User Class")

                    self.load_tab_content()
                    
                    # Enable Refresh Button
                    self.enable_refresh_button()
                    logger.debug("Enabled Refresh Button")
                    self.refresh_button.setText("Refresh")

            # If default user is not set
            else:
                logger.warning("No default user was found in config")
                self.disable_refresh_button()
                logger.debug("Refresh Button Disabled")
        else:
            logger.error("Credentials in the config are either missing or invalid.")

    def setupUi(self):
        self.resize(900, 700)
        self.setMinimumSize(870, 400)
        logger.debug(f"Set Window Size to 900,700 and minimum size to 870, 400")
        self.centralwidget = QWidget(self)
        logger.debug("Created Central Widget")

        self.verticalLayout = CustomVLayout(self.centralwidget, (6,6,6,6), spacing=6)
    
        self.alert_frame = QFrame(self.centralwidget)
        self.alert_frame.setMinimumSize(QtCore.QSize(100, 80))
        logger.debug("Created Alert Frame")

        self.horizontalLayout_2 = CustomHLayout(self.alert_frame, (6,6,6,6), 6)
        self.label = CustomLabel(self.alert_frame, color='rgb(236,18,32)', padding=(1,12,1,1))

        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = CustomLabel(self.alert_frame, minSize=(0, 0))
        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.alert_frame)

        self.search_box = QFrame(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(0, 80))
        self.search_box.setMaximumSize(QtCore.QSize(16777215, 90))

        self.horizontalLayout = CustomHLayout(self.search_box,(50, -1, 50, -1),20)

        self.search_field = QLineEdit(self.search_box)
        self.horizontalLayout.addWidget(self.search_field)

        self.searchButton = QPushButton(self.search_box)
        self.horizontalLayout.addWidget(self.searchButton)

        self.verticalLayout.addWidget(self.search_box)

        # Tabs
        self.tabWidget = QTabWidget(self.centralwidget)

        self.recent_activity_tab = QWidget()
        self.verticalLayout_3 = CustomVLayout(self.recent_activity_tab, (0, 6, 0, 0), 6)
        self.tabWidget.addTab(self.recent_activity_tab, "Recent Activity")

        self.recent_scores_tab = QWidget()
        self.verticalLayout_4 = CustomVLayout(self.recent_scores_tab, (0, 6, 0, 0), 6)
        self.tabWidget.addTab(self.recent_scores_tab, "Recent Score")

        self.user_tab = QWidget()
        self.verticalLayout_5 = CustomVLayout(self.user_tab, (0, 6, 0, 0), 6)
        self.tabWidget.addTab(self.user_tab, "User")

        self.search_tab = QWidget()
        self.tabWidget.addTab(self.search_tab, "Search")

        self.verticalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)

        self.refresh_button = QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.refresh_button)

        # Menubar
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 38))

        self.menuPreferences = QMenu(self.menubar)
        self.actionSettings = QAction(self)
        self.menuPreferences.addAction(self.actionSettings)

        self.menuAbout = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.actionGithub = QAction(self)

        self.actionAbout_OsuStatQt = QAction(self)

        self.menuAbout.addAction(self.actionGithub)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_OsuStatQt)

        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.tabWidget.setCurrentIndex(0)

        # Statusbar
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

    def setupText(self):
        self.refresh_button.setText("Loading...")
        self.setWindowTitle("OsuStatQt")
        self.label.setText("You haven\'t setup credentials")
        self.label_2.setText("In order for this application to work please go to the settings window (Preferences > Settings and enter the API credentials.")
        self.search_field.setPlaceholderText("type to search")
        self.searchButton.setText("Search")
        self.menuPreferences.setTitle("Preferences")
        self.actionSettings.setText("Settings")
        self.menuAbout.setTitle("Help")
        self.actionGithub.setText("Github")
        self.actionAbout_OsuStatQt.setText("About OsuStatQt")

    def setupStyle(self):
        self.setStyleSheet("""
            background-color: #1C1719;
            color:rgb(255,255,255);
            font: 63 9pt \"Torus Pro SemiBold\";
        """)

        self.alert_frame.setStyleSheet("""
        QFrame {
            background:rgba(135, 0, 0, 70);
            border-radius: 30px;
            }
        """)

        self.label.setStyleSheet("""
            background: none;
            font: 63 10pt \"Torus Pro SemiBold\";
            border-style: none;
            border-right-style: solid;
            border-color: rgb(236,18,32);
            border-width: 3px;
            padding-right: 12px;
        """)

        self.search_box.setStyleSheet("""
            QFrame{
                background-color: #46383E;
                border-radius: 7px;
            }
            QLineEdit {
                background-color: #46383E;
            }
        """)

        self.search_field.setStyleSheet("""
            border-style:none;
            border-bottom-style: solid;
            border-color: gray;
            border-width: 2px;
            font: 63 14pt \"Torus Pro SemiBold\";
            padding-bottom: 5px
        """)

        self.searchButton.setStyleSheet("""
            QPushButton {
                background-color: #AC396D;
                border:none;
                border-radius: 20px;
                font: 63 12pt \"Torus Pro SemiBold\";
                padding: 10px;
                min-width:80px
            }
            QPushButton:hover {
                background-color: #FF66AB;
            }
        """)

        self.tabWidget.setStyleSheet("""
            QTabWidget:pane {
                border:none;
            }
            QTabBar::tab {
                background: #392E33;
                padding:12px;
                min-width: 100px;
            }
            QTabBar::tab::selected {
                background: rgb(172, 57, 109);
            }
            """)

        self.menubar.setStyleSheet("""
            QMenuBar {
                font: 63 10pt \"Torus Pro SemiBold\";
                padding: 8px;
                background-color: rgb(172, 57, 109);
            }
            QMenuBar::item {
                color: rgb(223, 223, 223)
            }
            QMenuBar::item:selected {
                color: rgb(255,255,255);
                background-color: rgb(172, 57, 109);
            }
            QMenu {
                background-color:rgb(172, 57, 109);
            }
            QMenu::item {
                background-color: transparent;
            }

            QMenu::item::selected {
                background: #2a2327;
            }
        """)

        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(122, 86, 103);
                color: rgb(200, 200, 200);
                border:none;
                border-radius: 7px;
                font: 63 12pt \"Torus Pro SemiBold\";
                padding: 10px;
                min-width:80px
            }
        """)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)


    assetpath = Path(__file__).parent / "Assets"
    logger.info(f"Asset Path set as: {assetpath}")

    app.setWindowIcon(QtGui.QIcon(f'{assetpath}/Logo/icon48x.ico'))

    try:
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-SemiBold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Regular.ttf")
    except: logger.error("Could not load fonts")
    else: logger.debug("Fonts loaded")

    ui = MainWindow()
    sys.exit(app.exec_())
