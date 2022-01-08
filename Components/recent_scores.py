
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from functions import get_time_elapsed


class RecentScoreItem(QWidget):
	def __init__(self, score):
		super().__init__() 
		self.show_UI()
		self.setStyles()
		self.setConnections(score)

	
	def mousePressEvent(self, event):
		if self.accuracy_box.isVisible() == False:
			print("Showing accuracy Box")
			self.accuracy_box.setVisible(True)
			self.setMinimumSize(796, 88)
		else:
			print("Hiding Accuracy Box")
			self.accuracy_box.setVisible(False)
			self.setMinimumSize(796, 60)
	
	def setConnections(self, score):

		# Set grade image
		if not score.passed:
			self.rank_grade_label.setPixmap(QtGui.QPixmap("Assets/Rank_Grades/F.png"))
		else:
			_grade = str(score.rank).split("Grade.")[1]
			print("Grade is: ", _grade)
			self.rank_grade_label.setPixmap(QtGui.QPixmap(f"Assets/Rank_Grades/{_grade}.png"))
		
		# Show mods
		mods = str(score.mods)
		mods = [*map(''.join, zip(mods[::2], mods[1::2]))] # Split mods sring into individual mod names
		if 'NM' not in mods:
			sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			for mod in mods:
				try:
					self.mod_icon = QLabel(self.innerscore_box)
					self.mod_list.addWidget(self.mod_icon)
					sizePolicy.setHeightForWidth(self.mod_icon.sizePolicy().hasHeightForWidth())
					self.mod_icon.setSizePolicy(sizePolicy)
					self.mod_icon.setMaximumSize(QtCore.QSize(36, 26))
					self.mod_icon.setScaledContents(True)
					self.mod_icon.setObjectName("mod_icon")
					self.mod_icon.setPixmap(QtGui.QPixmap(f"ssets/Mod_Icons/{mod}.png"))
				except:
					print("Mod Icon Not found")
		
		self.accuracy_box.setVisible(False)
		
		self.beatmap_title.setText(score.beatmapset.title)
		self.beatmap_subtext_label.setText(f"{score.beatmap.version}     {get_time_elapsed(score.created_at)}")
		self.accuracy_label.setText(f"{score.accuracy*100:.2f}%")
		self.weighted_pp_label.setText("")
		if score.pp is not None:
			self.unweighted_pp_label.setText(f"{score.pp:.1f}pp")
		else:
			self.unweighted_pp_label.setText(f"   --   ")
		

	def show_UI(self):

		# Set widget Layout
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		# Set Size Constraints
		self.setMinimumSize(QtCore.QSize(750, 60))
		self.setMaximumSize(QtCore.QSize(16777215, 88))
		self.verticalLayout = QVBoxLayout(self)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")


		self.scorebox = QFrame(self)
		self.scorebox.setMinimumSize(QtCore.QSize(0, 60))
		self.scorebox.setMaximumSize(QtCore.QSize(16777215, 60))
		self.scorebox.setFrameShape(QFrame.StyledPanel)
		self.scorebox.setFrameShadow(QFrame.Raised)
		self.scorebox.setObjectName("scorebox")

		self.horizontalLayout = QHBoxLayout(self.scorebox)
		self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		
		self.innerscore_box = QFrame(self.scorebox)
		self.innerscore_box.setFrameShape(QFrame.StyledPanel)
		self.innerscore_box.setFrameShadow(QFrame.Raised)
		self.innerscore_box.setObjectName("innerscore_box")

		self.horizontalLayout_2 = QHBoxLayout(self.innerscore_box)
		self.horizontalLayout_2.setContentsMargins(-1, 4, 20, 4)
		self.horizontalLayout_2.setSpacing(16)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")

		self.rank_grade_label = QLabel(self.innerscore_box)
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.rank_grade_label.sizePolicy().hasHeightForWidth())
		self.rank_grade_label.setSizePolicy(sizePolicy)
		self.rank_grade_label.setMaximumSize(QtCore.QSize(44, 16777215))
		self.rank_grade_label.setText("")
		self.rank_grade_label.setScaledContents(True)
		self.rank_grade_label.setObjectName("rank_grade_label")
		self.horizontalLayout_2.addWidget(self.rank_grade_label)

		self.beatmap_info_box = QVBoxLayout()
		self.beatmap_info_box.setSpacing(0)
		self.beatmap_info_box.setObjectName("beatmap_info_box")

		self.beatmap_title = QLabel(self.innerscore_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.beatmap_title.sizePolicy().hasHeightForWidth())

		self.beatmap_title.setSizePolicy(sizePolicy)
		self.beatmap_title.setMaximumSize(QtCore.QSize(16777215, 30))
		self.beatmap_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
		self.beatmap_title.setObjectName("beatmap_title")
		self.beatmap_info_box.addWidget(self.beatmap_title)
		self.beatmap_subtext_label = QLabel(self.innerscore_box)
		self.beatmap_subtext_label.setMinimumSize(QtCore.QSize(0, 25))
		self.beatmap_subtext_label.setObjectName("beatmap_subtext_label")
		self.beatmap_info_box.addWidget(self.beatmap_subtext_label)
		self.horizontalLayout_2.addLayout(self.beatmap_info_box)
		spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)

		self.mod_list = QHBoxLayout()
		self.mod_list.setSpacing(4)
		self.mod_list.setObjectName("mod_list")

		self.horizontalLayout_2.addLayout(self.mod_list)
		self.accuracy_label = QLabel(self.innerscore_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.accuracy_label.sizePolicy().hasHeightForWidth())
		self.accuracy_label.setSizePolicy(sizePolicy)
		self.accuracy_label.setObjectName("accuracy_label")
		self.horizontalLayout_2.addWidget(self.accuracy_label)
		self.weighted_pp_label = QLabel(self.innerscore_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.weighted_pp_label.sizePolicy().hasHeightForWidth())
		self.weighted_pp_label.setSizePolicy(sizePolicy)
		self.weighted_pp_label.setObjectName("weighted_pp_label")
		self.horizontalLayout_2.addWidget(self.weighted_pp_label)
		self.horizontalLayout.addWidget(self.innerscore_box)
		self.unweighted_pp_label = QLabel(self.scorebox)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.unweighted_pp_label.sizePolicy().hasHeightForWidth())
		self.unweighted_pp_label.setSizePolicy(sizePolicy)
		self.unweighted_pp_label.setAlignment(QtCore.Qt.AlignCenter)
		self.unweighted_pp_label.setObjectName("unweighted_pp_label")
		self.horizontalLayout.addWidget(self.unweighted_pp_label)
		self.verticalLayout.addWidget(self.scorebox)

		self.accuracy_box = QFrame(self)
		self.accuracy_box.setMinimumSize(QtCore.QSize(0, 28))
		self.accuracy_box.setMaximumSize(QtCore.QSize(16777215, 28))
		self.accuracy_box.setFrameShape(QFrame.StyledPanel)
		self.accuracy_box.setFrameShadow(QFrame.Raised)
		self.accuracy_box.setObjectName("accuracy_box")
		self.horizontalLayout_3 = QHBoxLayout(self.accuracy_box)
		self.horizontalLayout_3.setContentsMargins(30, 4, 30, 4)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.accuracy_100_label = QLabel(self.accuracy_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.accuracy_100_label.sizePolicy().hasHeightForWidth())
		self.accuracy_100_label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Torus Pro Bold")
		font.setPointSize(10)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.accuracy_100_label.setFont(font)
		self.accuracy_100_label.setAlignment(QtCore.Qt.AlignCenter)
		self.accuracy_100_label.setObjectName("accuracy_100_label")
		self.horizontalLayout_3.addWidget(self.accuracy_100_label)
		self.accuracy_95_label = QLabel(self.accuracy_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.accuracy_95_label.sizePolicy().hasHeightForWidth())
		self.accuracy_95_label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Torus Pro Bold")
		font.setPointSize(10)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.accuracy_95_label.setFont(font)
		self.accuracy_95_label.setAlignment(QtCore.Qt.AlignCenter)
		self.accuracy_95_label.setObjectName("accuracy_95_label")
		self.horizontalLayout_3.addWidget(self.accuracy_95_label)
		self.accuracy_90_label = QLabel(self.accuracy_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.accuracy_90_label.sizePolicy().hasHeightForWidth())
		self.accuracy_90_label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Torus Pro Bold")
		font.setPointSize(10)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.accuracy_90_label.setFont(font)
		self.accuracy_90_label.setAlignment(QtCore.Qt.AlignCenter)
		self.accuracy_90_label.setObjectName("accuracy_90_label")
		self.horizontalLayout_3.addWidget(self.accuracy_90_label)
		self.accuracy_85_label = QLabel(self.accuracy_box)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.accuracy_85_label.sizePolicy().hasHeightForWidth())
		self.accuracy_85_label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Torus Pro Bold")
		font.setPointSize(10)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.accuracy_85_label.setFont(font)
		self.accuracy_85_label.setAlignment(QtCore.Qt.AlignCenter)
		self.accuracy_85_label.setObjectName("accuracy_85_label")
		self.horizontalLayout_3.addWidget(self.accuracy_85_label)
		self.verticalLayout.addWidget(self.accuracy_box)
		self.accuracy_100_label.setText("100%    ??pp")
		self.accuracy_95_label.setText("95%    ??pp")
		self.accuracy_90_label.setText("90%    ??pp")
		self.accuracy_85_label.setText("85%    ??pp")
	
	
	def setStyles(self):

		self.setStyleSheet("""
			background-color: #392E33; 
			color:rgb(255,255,255); 
			font: 63 9pt \"Torus Pro SemiBold\"; 
			border: none;
		""")

		self.scorebox.setStyleSheet("""
			background-color: #392E33;
		""")
		
		self.innerscore_box.setStyleSheet("""
			background-color: #46393f
		""")

		self.beatmap_title.setStyleSheet("""
			font: 63 10pt \"Torus Pro SemiBold\";
		""")

		self.accuracy_label.setStyleSheet("""
			color: #FECC20; 
			font: 75 11pt \"Torus Pro Bold\";
		""")

		self.weighted_pp_label.setStyleSheet("""
			font: 75 11pt \"Torus Pro Bold\";
		""")

		self.unweighted_pp_label.setStyleSheet("""
			color: #FF67AA; 
			font: 75 14pt \"Torus Pro Bold\";
		""")

		self.accuracy_box.setStyleSheet("""
			background-color: rgb(32,26,29); 
			font: 75 10pt \"Torus Pro Bold\";
		""")

		self.accuracy_100_label.setStyleSheet("""color: #0074FE""")
		self.accuracy_95_label.setStyleSheet("""color: #88DA20;""")
		self.accuracy_90_label.setStyleSheet("""color: #E5B538""")
