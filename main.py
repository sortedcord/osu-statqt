from PyQt5.QtWidgets import *
from scorecard import ScoreCard
import sys
from ossapi import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setGeometry(300,300,800,700)
        window_layout = QVBoxLayout()
        recent_playcard = ScoreCard()
        window_layout.addWidget(recent_playcard)
        self.setLayout(window_layout)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    execute = MainWindow()
    sys.exit(app.exec_())
