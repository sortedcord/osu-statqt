from PyQt5 import QtCore, QtWidgets

from Components.recent_activity import RecentActivityItem



class RecentActivityTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi()
        self.setupConnections(mainWindow)

    def setupConnections(self, mainWindow):
        for recent_activity in mainWindow.config.api.user_recent_activity(user_id=mainWindow.default_user_class.id, limit=20, offset=0):
            # print(recent_activity)
            widget = RecentActivityItem(mainWindow, recent_activity)
            self.verticalLayout_2.addWidget(widget)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(778, 352)
        self.setStyleSheet("""background-color: #2A2327;
                           color:rgb(255,255,255);
                           font: 63 9pt "Torus Pro"; 
                           border: none;""")
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
        self.scrollArea.setStyleSheet("""
        QScrollBar:vertical {
	border: none;
    background: rgb(45, 45, 68);
    width: 14px;
    margin: 15px 0 15px 0;
	border-radius: 0px;
 }

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {	
	background-color: #ac396d;
	min-height: 30px;
	border-radius: 0px;
}
QScrollBar::handle:vertical:hover{	
	background-color: rgb(255, 102, 171);
}
QScrollBar::handle:vertical:pressed {	
	background-color: rgb(255, 102, 171);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-top-left-radius: 0px;
	border-top-right-radius: 0px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {	
	background-color: rgb(255, 102, 171);
}
QScrollBar::sub-line:vertical:pressed {	
	background-color: rgb(255, 102, 171);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-bottom-left-radius: 0px;
	border-bottom-right-radius: 0px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {	
	background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:vertical:pressed {	
	background-color: rgb(255, 102, 171);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}



/* HORIZONTAL SCROLLBAR - HOMEWORK */
QScrollBar:horizontal {
   
}
QScrollBar::handle:horizontal {
    
}
QScrollBar::add-line:horizontal {
    
}
QScrollBar::sub-line:horizontal {
    
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{

}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{

}

        """)


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
        
