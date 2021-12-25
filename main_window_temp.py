from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 716)
        MainWindow.setMinimumSize(QtCore.QSize(744, 716))
        MainWindow.setMaximumSize(QtCore.QSize(744, 716))
        MainWindow.setStyleSheet("background-color: rgb(28,23,25);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 12, 726, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(726, 0))
        self.frame.setMaximumSize(QtCore.QSize(726, 80))
        self.frame.setStyleSheet("background-color: rgb(70,56,62);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(72, 28, 509, 31))
        font = QtGui.QFont()
        font.setFamily("Torus Pro SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(189,170,179);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(44, 32, 24, 24))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/search.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(588, 20, 97, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"font: 63 11pt \"Torus Pro SemiBold\";\n"
"color: white;\n"
"border-radius: 15;\n"
"background-color: rgb(172,57,109);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255,102,171);\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 160, 751, 509))
        self.frame_2.setStyleSheet("background-color: rgb(42,35,39);\n"
"color: rgb(255,255,255)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 110, 751, 40))
        self.frame_3.setStyleSheet("QFrame {background-color: rgb(42,35,39);\n"
"border-style: none;\n"
"border-bottom-style: solid;\n"
"border-width: 2px;\n"
"border-bottom-color: rgb(255,102,171);\n"
"border-top-style: none;\n"
"color: #fff;}\n"
"\n"
"QPushButton {\n"
"border: none;\n"
"color: white;\n"
"background-color: rgb(42,35,39);\n"
"    font: 63 12pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-style: none;\n"
"border-bottom-style: solid;\n"
"border-width: 7px;\n"
"border-bottom-color:  rgb(255,102,171);\n"
"\n"
"color: white;\n"
"background-color:rgb(42,35,39);\n"
"margin-top: 7px;\n"
"    font: 63 12pt \"Torus Pro SemiBold\";\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(129, 0, 129, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(8, 584, 729, 41))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"font: 63 11pt \"Torus Pro SemiBold\";\n"
"color: white;\n"
"border-radius: 15;\n"
"background-color: rgb(172,57,109);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255,102,171);\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 62))
        self.menubar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 57, 109, 255), stop:1 rgba(255, 255, 255, 0));\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"padding: 20px;\n"
"color: rgb(255,255,255);")
        self.menubar.setObjectName("menubar")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(42,35,39);\n"
"font: 9pt \"Torus Pro\";\n"
"color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuPreferences.addAction(self.actionSettings)
        self.menubar.addAction(self.menuPreferences.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "type to search"))
        self.pushButton_4.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Recent"))
        self.pushButton.setText(_translate("MainWindow", "Beatmap"))
        self.pushButton_2.setText(_translate("MainWindow", "User"))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
import Background_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
