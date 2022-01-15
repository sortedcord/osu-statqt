from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import requests


class CustomLabel(QLabel):
    def __init__(self,
                 parent,
                 text=None,
                 color='white',
                 font_size=10,
                 font_style='',
                 image_url=None,
                 minSize=(0, 0),
                 maxSize=(16777215, 16777215),
                 padding=(0, 0, 0, 0),
                 wordwrap=False,
                 background='none'
                 ):
        super().__init__(parent)

        if text is not None:
            self.setText(text)

        self.setStyleSheet(f"font: 75 {font_size}pt \"Torus Pro {font_style}\";\n"
                           f"color: {color}; \n"
                           f"background: {background}; \n"
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
