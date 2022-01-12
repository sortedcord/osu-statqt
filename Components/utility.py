from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class MsgBox(QMessageBox):
    def __init__(self, text, icon="information"):
        super().__init__()

        if icon == "critical":
            icon = QMessageBox.Critical
        elif icon == "warning":
            icon = QMessageBox.Warning
        elif icon == "information":
            icon = QMessageBox.Information
        elif icon == "question":
            icon = QMessageBox.Question

        self.setWindowTitle("OsuStatQt")
        self.setIcon(icon)
        self.setText(text)

        _ = self.exec_()

class CustomSizePolicy(QSizePolicy):
    def __init__(self, horizontalPolicy, verticalPolicy, parent):
        super().__init__()

        self.setHorizontalPolicy(horizontalPolicy)
        self.setVerticalPolicy(verticalPolicy)

        self.setHorizontalStretch(0)
        self.setVerticalStretch(0)

        self.setHeightForWidth(parent.sizePolicy().hasHeightForWidth())

        parent.setSizePolicy(self)


class CustomVLayout(QVBoxLayout):
    def __init__(self, parent, margins=(0,0,0,0), spacing=0):
        super().__init__(parent)

        # Set Margins
        _1, _2, _3, _4 = margins
        self.setContentsMargins(_1,_2,_3,_4)

        self.setSpacing(spacing)


class CustomHLayout(QHBoxLayout):
    def __init__(self, parent, margins=(0,0,0,0), spacing=0):
        super().__init__(parent)

        # Set Margins
        _1, _2, _3, _4 = margins
        self.setContentsMargins(_1,_2,_3,_4)

        self.setSpacing(spacing)




