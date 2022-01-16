from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from Components.css_files import scrollbar_style
from Components.layouts import CustomHLayout
from Components.controls import CustomLabel

from utils import get_time_elapsed

from loguru import logger
import ossapi

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

class RecentActivityItem(QWidget):
	def __init__(self, mainWindow, activity):
		super().__init__()        

		# Set Widget Constraints
		self.resize(778, 26)
		self.setMinimumSize(QtCore.QSize(770, 0))
		self.setMaximumSize(QtCore.QSize(1920, 26))

		# Set Widget Layout
		self.horizontalLayout = CustomHLayout(self, (3, 3, 3, 3), 6)

		# Set RankScore Label (Grade)
		self.rank_score_label = CustomLabel(self, maxSize=(30,14), minSize=(30,14))
		self.horizontalLayout.addWidget(self.rank_score_label)

		# Set Usrername
		self.username = CustomLabel(self, color="rgb(210,160,184)", font_style="Bold", text=mainWindow.config.default_user.username)
		self.horizontalLayout.addWidget(self.username)

		# Set Event Description (Beatmap Name)
		self.event_description_label = CustomLabel(self)
		self.horizontalLayout.addWidget(self.event_description_label)

		# Set Event Type
		self.event_type = CustomLabel(self, color="rgb(210,160,184)", font_style="Bold")
		self.horizontalLayout.addWidget(self.event_type)

		# Set Gamemode Label
		self.gamemode_label = CustomLabel(self)
		self.horizontalLayout.addWidget(self.gamemode_label)

		spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)

		# Time Label
		self.datetime_label = CustomLabel(self, color="rgb(129,112,121)", text=get_time_elapsed(activity.created_at))
		self.horizontalLayout.addWidget(self.datetime_label)

		if type(activity) == ossapi.models.RankEvent:
			self.event_description_label.setText(f" achieved rank # {activity.rank} on ")
			self.event_type.setText(f"{activity.beatmap.title} ")
			self.gamemode_label.setText("(osu!)")
            
			self.rank_score_label.setPixmap(QtGui.QPixmap(f"{mainWindow.assetpath}/Rank_Grades/{str(activity.scoreRank).replace('X','SS')}.png"))

		elif type(activity) == ossapi.models.RankLostEvent:
			self.event_description_label.setText(f" has lost first place on ")
			self.event_type.setText(f"{activity.beatmap.title} ")
			self.gamemode_label.setText("(osu!)")
			self.rank_score_label.setPixmap(QtGui.QPixmap(None))
		
		elif type(activity) == ossapi.models.UserSupportAgainEvent:
			self.event_description_label.setText(f" has bought osu! supporter")
			self.event_type.setText("")
			self.gamemode_label.setText("")
			self.rank_score_label.setPixmap(QtGui.QPixmap(None))
		
		elif 'Achievement' in str(type(activity)):
			self.event_description_label.setText(f" unlocked the '{activity.achievement.name}' medal!")
			self.event_type.setText("")
			self.gamemode_label.setText("")
			self.rank_score_label.setPixmap(QtGui.QPixmap(None))
		else:
			self.event_description_label.setText(f" performed an unrecognized event.")

		self.setStyleSheet("background-color: #2A2327;color:rgb(255,255,255);font: 63 9pt \"Torus Pro SemiBold\";border: none;")
