from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import requests

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

        self.setContentsMargins(*margins)
        self.setSpacing(spacing)


class CustomHLayout(QHBoxLayout):
    def __init__(self, parent, margins=(0,0,0,0), spacing=0):
        super().__init__(parent)

        self.setContentsMargins(*margins)
        self.setSpacing(spacing)

class CustomLabel(QLabel):
    def __init__(self, parent, text=None, color='white', font_size=10, font_style='', image_url=None, minSize=(0,0), maxSize=(16777215,16777215), padding=(1,1,1,1), wordwrap=True):
        super().__init__(parent)

        if text is not None:
            self.setText(text)

        self.setStyleSheet(f"font: 75 {font_size}pt \"Torus Pro {font_style}\";\n"
                            f"color: {color}; \n"
                            # T R B L
                            f"background:  \n"
                            f"padding: {padding[0]} {padding[1]} {padding[2]} {padding[3]};")

        if image_url is not None:
            if 'http' in image_url:
                self.image = QtGui.QImage()
                self.image.loadFromData(requests.get(image_url).content)
                self.setPixmap(QtGui.QPixmap(self.image))
            else:
                self.setPixmap(QtGui.QPixmap(image_url))
            self.setScaledContents(True)
            self.setWordWrap(wordwrap)
                
        
        self.setMinimumSize(QtCore.QSize(*minSize))
        self.setMaximumSize(QtCore.QSize(*maxSize))




