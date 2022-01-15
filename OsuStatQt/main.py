from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from loguru import logger
from pathlib import Path

from mainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)


    assetpath = Path(__file__).parent / "Assets"
    logger.info(f"Asset Path set as: {assetpath}")

    app.setWindowIcon(QtGui.QIcon(f'{assetpath}/Logo/icon48x.ico'))

    try:
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-SemiBold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(f"{assetpath}/Fonts/TorusPro-Regular.ttf")

    except: logger.error("Could not load fonts")
    else: logger.debug("Fonts loaded")

    ui = MainWindow()
    sys.exit(app.exec_())
