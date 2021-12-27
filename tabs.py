from PyQt5 import QtCore, QtGui, QtWidgets


class RecentActivityTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)
        

    def setupConnections(self, mainWindow):
        # print(len(mainWindow.api.user_recent_activity(user_id=mainWindow.default_user.id, limit=10)))
        for recent_activity in mainWindow.api.user_recent_activity(user_id=mainWindow.default_user.id, limit=20):
            widget = QtWidgets.QLabel()
            if 'LostEvent' in str(type(recent_activity)):
                widget.setText(f"{mainWindow.default_user.username} lost first place on {recent_activity.beatmap.title}")
            elif 'UserSupportAgain' in str(type(recent_activity)):
                widget.setText(f"{mainWindow.default_user.username} Bought Supporter Again")
            else:
                widget.setText(f"{recent_activity.scoreRank}   {mainWindow.default_user.username} achieved rank #{recent_activity.rank} on {recent_activity.beatmap.title}")
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
