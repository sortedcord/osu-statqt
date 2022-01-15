from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

import ossapi
from Components.utility import *

from functions import get_time_elapsed


class RecentActivityItem(QWidget):
	def __init__(self, mainWindow, activity):
		super().__init__()        

		# Set Widget Constraints
		self.resize(778, 26)
		self.setMinimumSize(QtCore.QSize(770, 0))
		self.setMaximumSize(QtCore.QSize(1920, 26))

		# Set Widget Layout
		self.horizontalLayout = QHBoxLayout(self)
		self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
		self.horizontalLayout.setSpacing(6)

		# Set RankScore Label (Grade)
		self.rank_score_label = CustomLabel(self, maxSize=(30,14), minSize=(30,14))
		self.rank_score_label.setScaledContents(True)
		self.horizontalLayout.addWidget(self.rank_score_label)

		# Set Usrername
		self.username = CustomLabel(self, color="rgb(210,160,184)", font_style="Bold", text=mainWindow.config.compact_default_user.username)
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
			self.rank_score_label.setPixmap(QtGui.QPixmap(f"{mainWindow.assetpath}/Rank_Grades/{activity.scoreRank}.png"))

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
