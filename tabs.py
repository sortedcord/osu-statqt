from PyQt5 import QtCore, QtWidgets


class RecentActivityTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        for recent_activity in mainWindow.config.api.user_recent_activity(user_id=mainWindow.default_user_class.id, limit=20):
            widget = QtWidgets.QLabel()
            if 'LostEvent' in str(type(recent_activity)):
                widget.setText(
                    f"{mainWindow.default_user_class.username} lost first place on {recent_activity.beatmap.title}")
            elif 'UserSupportAgain' in str(type(recent_activity)):
                widget.setText(
                    f"{mainWindow.default_user_class.username} Bought Supporter Again")
            elif 'BeatmapsetUpdate' in str(type(recent_activity)):
                widget.setText(
                    f"{mainWindow.default_user_class.username} updated beatmapset {recent_activity.beatmapset.title}")
            elif 'BeatmapsetUpload' in str(type(recent_activity)):
                widget.setText(
                    f"{mainWindow.default_user_class.username} uploaded beatmapset {recent_activity.beatmapset.title}")
            elif 'Achievement' in str(type(recent_activity)):
                widget.setText(
                    f"{mainWindow.default_user_class.username} got some achievement")
            elif 'RankEvent' in str(type(recent_activity)):
                widget.setText(
                    f"{recent_activity.scoreRank}   {mainWindow.default_user_class.username} achieved rank #{recent_activity.rank} on {recent_activity.beatmap.title}")
            else:
                widget.setText("Unknown Event occured")
            self.verticalLayout_2.addWidget(widget)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
        self.setStyleSheet("background-color: #2A2327;\n"
                           "color:rgb(255,255,255);\n"
                           "font: 63 9pt \"Torus Pro SemiBold\";")
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


class RecentScoreTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        try:
            for recent_score in mainWindow.config.api.user_scores(mainWindow.default_user_class.id, 'recent'):
                widget = QtWidgets.QLabel()
                widget.setText(recent_score.beatmapset.title)
                self.verticalLayout_2.addWidget(widget)
        except:
            widget = QtWidgets.QLabel()
            widget.setText(
                f"Could not find any more recent scores for {mainWindow.default_user_class.username}")
            self.verticalLayout_2.addWidget(widget)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
        self.setStyleSheet("background-color: #2A2327;\n"
                           "color:rgb(255,255,255);\n"
                           "font: 63 9pt \"Torus Pro SemiBold\";")
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
