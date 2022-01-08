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
