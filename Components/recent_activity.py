from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import ossapi
import datetime

from functions import get_time_elapsed


class RecentActivityItem(QWidget):
	def __init__(self, mainWindow, activity):
		super().__init__()        

		self.resize(778, 26)
		self.setMinimumSize(QtCore.QSize(770, 0))
		self.setMaximumSize(QtCore.QSize(1920, 26))
		self.setStyleSheet("background-color: #2A2327;\n"
"                           color:rgb(255,255,255);\n"
"                           font: 63 9pt \"Torus Pro SemiBold\"; \n"
"                           border: none;")
		self.horizontalLayout = QHBoxLayout(self)
		self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
		self.horizontalLayout.setSpacing(6)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.rank_score_label = QLabel(self)
		self.rank_score_label.setMaximumSize(QtCore.QSize(30, 14))
		self.rank_score_label.setMinimumSize(QtCore.QSize(30, 14))
		self.rank_score_label.setText("")
		self.rank_score_label.setScaledContents(True)
		self.rank_score_label.setObjectName("rank_score_label")
		self.horizontalLayout.addWidget(self.rank_score_label)
		self.username = QLabel(self)
		self.username.setStyleSheet("""
			color: rgb(210,160,184);
			font: 75 10pt "Torus Pro Bold";
		""")
		self.username.setObjectName("username")
		self.horizontalLayout.addWidget(self.username)
		self.event_description_label = QLabel(self)
		self.event_description_label.setObjectName("event_description_label")
		self.horizontalLayout.addWidget(self.event_description_label)
		self.event_type = QLabel(self)
		self.event_type.setObjectName("event_type")
		self.event_type.setStyleSheet("""
			color: rgb(210,160,184);
			font: 75 10pt "Torus Pro Bold";
		""")
		self.horizontalLayout.addWidget(self.event_type)
		self.gamemode_label = QLabel(self)
		self.gamemode_label.setObjectName("gamemode_label")
		self.horizontalLayout.addWidget(self.gamemode_label)
		spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.datetime_label = QLabel(self)
		self.datetime_label.setStyleSheet("color: rgb(129,112,121);")
		self.datetime_label.setObjectName("datetime_label")
		self.horizontalLayout.addWidget(self.datetime_label)

		self.username.setText(mainWindow.default_user_class.username)

		if type(activity) == ossapi.models.RankEvent:
			self.event_description_label.setText(f" achieved rank # {activity.rank} on ")
			self.event_type.setText(f"{activity.beatmap.title} ")
			self.gamemode_label.setText("(osu!)")
			self.rank_score_label.setPixmap(QtGui.QPixmap(f".\\Components\\../Assets/Rank Grades/{activity.scoreRank}.png"))

		elif type(activity) == ossapi.models.RankLostEvent:
			self.event_description_label.setText(f" has lost first place on ")
			self.event_type.setText(f"{activity.beatmap.title} ")
			self.gamemode_label.setText("(osu!)")
			self.rank_score_label.setPixmap(QtGui.QPixmap(None))
		
		elif type(activity) == ossapi.models.UserSupportAgainEvent or type(activity) == ossapi.models.UserSupportEvent:
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
		
		

		self.datetime_label.setText(get_time_elapsed(activity.created_at))

		# self.show()


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = RecentActivityItem()
#     sys.exit(app.exec_())
