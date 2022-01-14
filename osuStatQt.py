from PyQt5 import QtCore, QtGui, QtWidgets
import os
from loguru import logger
from tabs.RecentActivityTab import RecentActivityTab

from functions import OsuStatUser
from config import load_config

from settings import SettingsWindow
from tabs_main import RecentScoreTab
from pathlib import Path

VERSION = '0.0.5'

class MainWindow(QtWidgets.QMainWindow):
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
        self.default_user_class = None
        logger.debug(f"Default User Class set to {self.default_user_class}")

        self.actionSettings.triggered.connect(self.showSettings)  # Settings Menu
        logger.debug("Connected settings menu to 'showSettings'")

        self.config = load_config()
        logger.debug("Config Loaded")

        # If credentials were valid
        if self.config.cred_verification_status == 'VERIFIED':
            self.statusbar.showMessage("Credentials verified")
            logger.info("Credentials Verified")

            self.alert_frame.setParent(None)  # Remove alert frame
            logger.debug("Alert Frame Removed")

            # If config has default user set
            if self.config.default_user is not None:
                logger.debug(f"Searching for user {self.config.default_user}")
                _uval = OsuStatUser(
                    self.config.api).search_user(self.config.default_user)
                
                # If Default User is valid
                if _uval != 0: 
                    
                    self.refresh_button.setText("Loading Data...")

                    logger.info(f"{self.config.default_user} found on Bancho")
                    self.default_user_class = OsuStatUser(self.config.api,self.config.default_user)
                    logger.debug("Created Default User Class")

                    self.load_tab_content()
                    
                    # Enable Refresh Button
                    self.enable_refresh_button()
                    logger.debug("Enabled Refresh Button")
                    self.refresh_button.setText("Refresh")
                else:
                    logger.error(f"{self.config.default_user} not found on Bancho")
                    self.disable_refresh_button()
                    logger.debug("Refresh Button Disabled")

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
        self.centralwidget = QtWidgets.QWidget(self)
        logger.debug("Created Central Widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
    
        self.alert_frame = QtWidgets.QFrame(self.centralwidget)
        self.alert_frame.setMinimumSize(QtCore.QSize(100, 80))
        self.alert_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alert_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        logger.debug("Created Alert Frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.alert_frame)
        self.label = QtWidgets.QLabel(self.alert_frame)

        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.alert_frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("background:none;")
        self.label_2.setWordWrap(True)
        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.alert_frame)

        self.search_box = QtWidgets.QFrame(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(0, 80))
        self.search_box.setMaximumSize(QtCore.QSize(16777215, 90))
        self.search_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_box)

        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout.setSpacing(20)

        self.search_field = QtWidgets.QLineEdit(self.search_box)
        self.horizontalLayout.addWidget(self.search_field)

        self.searchButton = QtWidgets.QPushButton(self.search_box)
        self.horizontalLayout.addWidget(self.searchButton)

        self.verticalLayout.addWidget(self.search_box)

        # Tabs

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        self.recent_activity_tab = QtWidgets.QWidget()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.recent_activity_tab)
        self.verticalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.tabWidget.addTab(self.recent_activity_tab, "")

        self.recent_scores_tab = QtWidgets.QWidget()
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.recent_scores_tab)
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 0)
        self.tabWidget.addTab(self.recent_scores_tab, "")

        self.user_tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.user_tab, "")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.user_tab)
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.tabWidget.addTab(self.user_tab, "")

        self.search_tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.search_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)

        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.refresh_button)

        # Menubar

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 38))

        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.actionSettings = QtWidgets.QAction(self)
        self.menuPreferences.addAction(self.actionSettings)

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.actionGithub = QtWidgets.QAction(self)

        self.actionAbout_OsuStatQt = QtWidgets.QAction(self)

        self.menuAbout.addAction(self.actionGithub)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_OsuStatQt)

        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.tabWidget.setCurrentIndex(0)

        # Statusbar

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

    def setupText(self):
        self.setWindowTitle("OsuStatQt")
        self.label.setText("You haven\'t setup credentials")
        self.label_2.setText(
            "In order for this application to work please go to the settings window (Preferences > Settings and enter the API credentials.")
        self.search_field.setPlaceholderText("type to search")
        self.searchButton.setText("Search")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.recent_activity_tab), "Recent Activity")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.recent_scores_tab), "Recent Scores")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.user_tab), "User")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.search_tab), "Search")
        self.menuPreferences.setTitle("Preferences")
        self.actionSettings.setText("Settings")
        self.menuAbout.setTitle("Help")
        self.actionGithub.setText("Github")
        self.actionAbout_OsuStatQt.setText("About OsuStatQt")
        self.refresh_button.setText("Refresh")

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
    app = QtWidgets.QApplication(sys.argv)
    if os.path.exists('icon48x.ico'):
        app.setWindowIcon(QtGui.QIcon('icon48x.ico'))
    else:
        app.setWindowIcon(QtGui.QIcon('Assets/Logo/icon48x.ico'))

    assetpath = Path(__file__).parent / "Assets"
    logger.info(f"Asset Path set as: {assetpath}")

    try:
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-SemiBold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Regular.ttf")
    except: logger.error("Could not load fonts")
    else: logger.debug("Fonts loaded")

    ui = MainWindow()
    sys.exit(app.exec_())
