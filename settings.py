from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from Components.settings import *
from Components.css_files import scrollbar_style
from Components.utility import MsgBox

from config import Config, del_config_file
from functions import OsuStatUser
import webbrowser
from loguru import logger

class SettingsWindow(QMainWindow):
    def __init__(self, mainWindow):
        super().__init__()

        self.mainWindow = mainWindow
        self.refresh_cooldown_values = [0, 5000, 10000, 15000, 30000, 60000] # time in milliseconds

        self.setupUi()
        logger.debug("Loaded Window UI Structure")
        self.setupText()
        self.setupStylesheet()
        logger.debug("Applied Stylesheet to Qt")
        self.load_data()
        logger.debug("Loaded Window Data")


    # <=============== Clicked Events ===============>
    def verify_credentials_clicked(self):
        logger.info("Executing Verify Credentials Button clicked event")

        mainWindow = self.mainWindow
        mainWindow.config.client_id = self.client_id_field.text()
        mainWindow.config.client_secret = self.client_secret_field.text()
        logger.debug(f"Verifying {mainWindow.config.client_id},{mainWindow.config.client_secret} ")
        mainWindow.config.verify_credentials()

        # If credentials are correct
        if mainWindow.config.cred_verification_status == 'VERIFIED':
            logger.success("Credentials have been verified.")

            # Disable Text Fields
            logger.debug("Locked Text Fields")
            self.client_id_field.setEnabled(False)
            self.client_secret_field.setEnabled(False)

            # Hide verify Button
            logger.debug("Set Credentials button visibility to False")
            self.verify_credentials_button.setVisible(False)

            logger.debug("Remove Alert Frame")
            mainWindow.alert_frame.setParent(None)

            MsgBox("Authenticated Successfully, you may use this client now.", 'information')

            # Refresh Settings Window
            logger.debug("Remove Alert Frame")
            self.load_data()

        # If invalid credentials
        else:
            logger.error("Entered credentials are invalid")
            mainWindow.config.cred_verification_status = 'INVALID'
            logger.info(f"Updated Login credentials to {mainWindow.config.cred_verification_status}")
            MsgBox("Invalid Credentials. Please Try Again.", 'critical')
        
        # Refresh Settings Window
        self.load_data()
        logger.error("Reloaded settings Window fields")


    def get_credentials_clicked(self):
        logger.info("Get Credentials button click event performed")
        webbrowser.open("https://osu.ppy.sh/home/account/edit")
        logger.info("Opening Link in Browser")


    def save_config_clicked(self):
        logger.info("Save Config Button Click Event Triggered")

        mainWindow = self.mainWindow

        if mainWindow.config.cred_verification_status == 'VERIFIED':

            if mainWindow.config.default_user != self.default_user_field.text():
                logger.debug("Change in default user detected")
                self.save_default_user()
                logger.info("Default User Saved")

            
            if mainWindow.config.refresh_cooldown != self.refresh_cooldown_values[self.refresh_limit_combo.currentIndex()]:
                logger.debug("Change in refresh cooldown  detected")
                self.save_refresh_cooldown()
                logger.info("refresh cooldown Saved")
            
            if mainWindow.config.show_failed_scores != self.toggle_failed_scores_checkbox.isChecked():
                logger.debug("Change in failed scores option")
                self.toggled_failed_scores()
                logger.info(f"Set Failed Scores to {mainWindow.config.show_failed_scores} in config")
        
        else:
            MsgBox("Please verify API credentials first.", "critical")


    def reset_config_clicked(self):
        mainWindow = self.mainWindow

        # Set MainWindow to new config instance
        mainWindow.config = Config()
        logger.info("Reset config instance")

        # Delete existing config file
        del_config_file()
        logger.info("Deleted Config File")

        # Reset Fields
        self.client_id_field.setText(None)
        self.client_secret_field.setText(None)
        self.default_user_field.setText(None)
        self.refresh_limit_combo.setCurrentIndex(3)
        logger.debug("Fields have been reset")

        # Load settings again
        self.load_data()
        


    def toggled_failed_scores(self):
        mainWindow = self.mainWindow

        mainWindow.config.show_failed_scores = self.toggle_failed_scores_checkbox.isChecked()


    # <=============== Save Events ===============>
    def save_default_user(self):
        mainWindow = self.mainWindow

        _id = OsuStatUser(mainWindow.config.api).search_user(self.default_user_field.text())

        if _id == 0:  # If no user is found in Bancho
            logger.error(f"{self.default_user_field.text()} was not found in Bancho")
            MsgBox('Specified user not found. Try checking your spelling.')

        else:  # If user is found
            logger.success("Specified User found.")
            mainWindow.default_user_class = OsuStatUser(mainWindow.config.api, id=_id)
            mainWindow.config.default_user = mainWindow.default_user_class.username
            logger.success(f"Default user set as {mainWindow.default_user_class.username}")
            MsgBox(f"Default user has been set as {mainWindow.default_user_class.username}", "information")

            self.default_user_field.setText(mainWindow.default_user_class.username)

            mainWindow.enable_refresh_button()
    

    def save_refresh_cooldown(self):
        if self.refresh_limit_combo.currentIndex() < 2:
            MsgBox("""Although you can, but it is highly recommended not to set the refresh cooldown value below 10 seconds as it may cause spamming of the refresh button.""", 'information')
        self.mainWindow.config.refresh_cooldown = self.refresh_cooldown_values[self.refresh_limit_combo.currentIndex()]



    # <=============== Other Functions ===============>
    def ulock_panels(self, state):
        self.default_user_panel.setEnabled(state)
        self.osuStat_panel.setEnabled(state)


    def load_data(self):
        mainWindow= self.mainWindow

        # If credentials verified
        if mainWindow.config.cred_verification_status == 'VERIFIED':
            self.ulock_panels(True)

            self.client_id_field.setText(str(mainWindow.config.client_id))
            self.client_secret_field.setText(mainWindow.config.client_secret)
            self.toggle_failed_scores_checkbox.setChecked(mainWindow.config.show_failed_scores)
            logger.debug("Filled in Fields")

            # Disable Credentials Field
            self.client_id_field.setEnabled(False)
            self.client_secret_field.setEnabled(False)
            logger.debug("Locked Credentials Fields")

            # Hide verify credentials button
            self.verify_credentials_button.setVisible(False)
            logger.debug(f"Verify Credentials Button Visibility > {self.verify_credentials_button.isVisible}")

            # Load Default User
            if mainWindow.default_user_class is not None:
                self.default_user_field.setText(mainWindow.default_user_class.username)
                logger.debug(f"Default User Field set to {mainWindow.default_user_class.username}")
            else:
                logger.debug(f"Disabled Refresh Button on MainWindow.")
                mainWindow.disable_refresh_button()

        # If credentials not verified
        else:
            logger.debug("Credentials Not Verified. Locking Other Panels")
            self.ulock_panels(False)
            logger.debug("Disabled Refresh Button")
            mainWindow.disable_refresh_button()
        
        # Load Refresh Cooldown
        try:
            self.refresh_limit_combo.setCurrentIndex(self.refresh_cooldown_values.index(mainWindow.config.refresh_cooldown))
        except IndexError:
            logger.error("That value of refresh cooldown is not supported")



    def setupUi(self):
        # Window Layout
        self.resize(800, 439)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.window_layout = QVBoxLayout(self.centralwidget)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setSpacing(0)


        # Top Title Bar
        self.top_bar_frame = QFrame(self.centralwidget)
        self.top_bar_frame.setMinimumSize(QtCore.QSize(800, 49))
        self.top_bar_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)

        # Title Bar Layout
        self.title_bar_layout = QHBoxLayout(self.top_bar_frame)
        self.title_bar_layout.setSpacing(12)
        self.window_layout.addWidget(self.top_bar_frame)

        # Title Bar Content
        self.title_label = QLabel(self.top_bar_frame)
        self.title_bar_layout.addWidget(self.title_label)

        # Reset Config Button
        self.reset_config_button = SettingsButton("Reset Config", "rgb(204,51,51)", "rgb(234,71,70)")
        self.reset_config_button.clicked.connect(lambda: self.reset_config_clicked())
        self.title_bar_layout.addWidget(self.reset_config_button)

        # Save Config Button
        self.save_config_button = SettingsButton("Save Config")
        self.save_config_button.clicked.connect(lambda: self.save_config_clicked())
        self.title_bar_layout.addWidget(self.save_config_button)

        # Settings Scrollable Area
        self.settings_scrollable_area = QScrollArea(self.centralwidget)
        self.settings_scrollable_area.setWidgetResizable(True)
        self.settings_scrollable_area.setStyleSheet(scrollbar_style)
        self.window_layout.addWidget(self.settings_scrollable_area)


        # Settings Content
        self.settings_content_frame = QFrame()
        self.settings_content_frame.setStyleSheet("border:none;")
        self.settings_content_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_content_frame.setFrameShadow(QFrame.Raised)
        self.settings_scrollable_area.setWidget(self.settings_content_frame)

        # Settings Content Layout
        self.settings_layout = QVBoxLayout(self.settings_content_frame)
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_layout.setSpacing(5)

        # Credentials Panel
        self.credentials_panel = SettingsPanel('Credentials')
        
        # Client ID
        self.client_id_label = SettingsLabel('client ID')
        self.client_id_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.credentials_panel.form_frame_layout.setWidget(0, QFormLayout.LabelRole, self.client_id_label)

        self.client_id_field = SettingsField()
        self.credentials_panel.form_frame_layout.setWidget(0, QFormLayout.FieldRole, self.client_id_field)

        # Client Secret
        self.client_secret_label = SettingsLabel('client secret')
        self.credentials_panel.form_frame_layout.setWidget(1, QFormLayout.LabelRole, self.client_secret_label)

        self.client_secret_field = SettingsField()
        self.credentials_panel.form_frame_layout.setWidget(1, QFormLayout.FieldRole, self.client_secret_field)

        # Submit Credentials Button
        self.verify_credentials_button = SettingsButton('Verify')
        self.credentials_panel.form_frame_layout.setWidget(6, QFormLayout.FieldRole, self.verify_credentials_button)
        self.verify_credentials_button.clicked.connect(lambda: self.verify_credentials_clicked())

        # Get Credentials Button
        self.get_credentials_button = SettingsButton('Get Credentials')
        self.credentials_panel.form_frame_layout.setWidget(7, QFormLayout.FieldRole, self.get_credentials_button)
        self.get_credentials_button.clicked.connect(lambda: self.get_credentials_clicked())


        self.settings_layout.addWidget(self.credentials_panel)


        # Default User Panel
        self.default_user_panel = SettingsPanel('User')

        # Set Default User Label
        self.default_user_label = SettingsLabel('user')
        self.default_user_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)   
        self.default_user_panel.form_frame_layout.setWidget(0, QFormLayout.LabelRole, self.default_user_label)

        self.default_user_field = SettingsField()
        self.default_user_panel.form_frame_layout.setWidget(0, QFormLayout.FieldRole, self.default_user_field)


        self.settings_layout.addWidget(self.default_user_panel)


        # OsuStat Panel
        self.osuStat_panel = SettingsPanel('OsuStat')
        
        # Refresh Cooldown
        self.refresh_cooldown_label = SettingsLabel('refresh cooldown')
        self.refresh_cooldown_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.osuStat_panel.form_frame_layout.setWidget(0, QFormLayout.LabelRole, self.refresh_cooldown_label)

        self.refresh_limit_combo = QComboBox()
        self.refresh_limit_combo.setObjectName("refresh_limit_combo")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.osuStat_panel.form_frame_layout.setWidget(0, QFormLayout.FieldRole, self.refresh_limit_combo)

        # Toggle Failed Scores
        self.toggle_failed_scores = SettingsLabel('show failed scores')
        self.toggle_failed_scores.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.osuStat_panel.form_frame_layout.setWidget(1, QFormLayout.LabelRole, self.toggle_failed_scores)

        # Toggle Failed Scores check box
        self.toggle_failed_scores_checkbox = QCheckBox()
        self.toggle_failed_scores_checkbox.setIconSize(QtCore.QSize(42, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_failed_scores_checkbox.sizePolicy().hasHeightForWidth())
        self.toggle_failed_scores_checkbox.setSizePolicy(sizePolicy)
        self.toggle_failed_scores_checkbox.setText("")
        self.osuStat_panel.form_frame_layout.setWidget(1, QFormLayout.FieldRole, self.toggle_failed_scores_checkbox)


        self.settings_layout.addWidget(self.osuStat_panel)

        

    def setupText(self):
        self.setWindowTitle("Settings | OsuStatQt")
        self.title_label.setText("      settings")
        self.refresh_limit_combo.setItemText(0, "No Limit")
        self.refresh_limit_combo.setItemText(1, "Every 5 Seconds")
        self.refresh_limit_combo.setItemText(2, "Every 10 Seconds")
        self.refresh_limit_combo.setItemText(3, "Every 15 Seconds")
        self.refresh_limit_combo.setItemText(4, "Every 30 Seconds")
        self.refresh_limit_combo.setItemText(5, "Every Minute")
    


    def setupStylesheet(self):
        self.setStyleSheet("""
            background-color:rgb(24,22,29);
            color: rgb(255,255,255);
            padding:0px;
        """)

        self.top_bar_frame.setStyleSheet("""
            background-color: rgb(35,31,47);
        """)

        self.title_label.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";")    

        self.refresh_limit_combo.setStyleSheet("""
            background-color: rgb(61, 57, 70);
            border: none;
            padding: 6px;
            border-radius: 4px;
            color: rgb(255,255,255);
            font: 63 10pt \"Torus Pro SemiBold\";
        """)

        self.toggle_failed_scores_checkbox.setStyleSheet("""
            background-color:rgb(49,47,56);
        """)
                                     

