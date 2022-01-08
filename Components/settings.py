from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class SettingsPanel(QFrame):
    def __init__(self, title):
        super().__init__()
        self.setupUi(title)
        self.setupStyle()

    def setupUi(self, title):
        # self.setMinimumSize(QtCore.QSize(798, 249))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        # Credentials Layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Credentials Panel Title
        self.title = QLabel(self)
        self.title.setMinimumSize(QtCore.QSize(240, 0))
        self.title.setMaximumSize(QtCore.QSize(240, 16777215))
        self.title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.title.setText(title)
        self.layout.addWidget(self.title)
        
        # Credentials Form Frame
        self.form_frame = QFrame()
        self.form_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.form_frame.setFrameShape(QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QFrame.Raised)

        # Credentials Form Frame Layout
        self.form_frame_layout = QFormLayout(self.form_frame)
        self.form_frame_layout.setContentsMargins(50, 30, 50, 50)
        self.form_frame_layout.setHorizontalSpacing(18)

        self.layout.addWidget(self.form_frame)
    
    def setupStyle(self):
        self.title.setStyleSheet("""
            font: 63 18pt \"Torus Pro SemiBold\";
            background-color:rgb(36,35,43);
            padding-left: 30px""")
        
        self.form_frame.setStyleSheet("""
            QFrame {
            background-color:rgb(49,47,56);
            font: 63 12pt \"Torus Pro SemiBold\";
            color: rgb(148, 143, 163);
            }
        """)
        

class SettingsButton(QPushButton):
    def __init__(self, text, default_color="rgb(86,57,172)", hover_color="rgb(140, 102, 255)", disabled_color="rgb(60,57,71)"):
        super().__init__()

        self._text = text
        self._default_color = default_color
        self._hover_color = hover_color
        self._disabled_color = disabled_color

        self.enabled_style = ("\n"
            "QPushButton {\n"
            f"       background-color: {default_color};\n"
            "        color: rgb(255, 255, 255);\n"
            "        padding: 6px;\n"
            "        border-radius:8px;\n"
            "        max-width:110px;\n"
            "        text-align: center;\n"
            "        font: 63 10pt \"Torus Pro SemiBold\"; \n"
            "}\n"    
            "QPushButton:hover {    \n"
                f"background-color: {hover_color};\n"
            "}\n")
        
        self.disabled_style = ("\n"
            "QPushButton {\n"
            f"       background-color: {self._disabled_color};\n"
            "        color: rgb(255, 255, 255);\n"
            "        padding: 6px;\n"
            "        border-radius:8px;\n"
            "        max-width:110px;\n"
            "        text-align: center;\n"
            "        font: 63 10pt 'Torus Pro SemiBold'; \n"
            "}\n")


        self.setText(text)
        self.setStyleSheet(self.enabled_style)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(160, 0))
    
    def disable(self):
        self.setDisabled(True)
        self.setStyleSheet()
    
    def enable(self):
        self.setDisabled(False)
        self.setStyleSheet(self.disabled_style)


class SettingsField(QLineEdit):
    def __init__(self, text=None, placeholder=None):
        super().__init__()

        self.setText(text)
        self.setPlaceholderText(placeholder)

        self.enabled_style = ("""
            QLineEdit {
                background-color: rgb(61, 57, 70);
                border: none;
                padding: 6px;
                border-radius: 4px;
                color: rgb(255,255,255);
                font: 63 10pt \"Torus Pro SemiBold\";
            }
            
            QLineEdit:focus {
                border-style: solid;
                border-width: 2px;
                border-color:  rgb(148, 143, 163);
            }
        """)

        self.setStyleSheet(self.enabled_style)


class SettingsLabel(QLabel):
    def __init__(self, text=None):
        super().__init__()

        self.setText(text)

        self.setStyleSheet("""
            font: 63 12pt \"Torus Pro SemiBold\";
        """)
