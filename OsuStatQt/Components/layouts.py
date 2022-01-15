from PyQt5.QtWidgets import (QSizePolicy, QVBoxLayout, QHBoxLayout)

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