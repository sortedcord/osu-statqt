from loguru import logger
from pathlib import Path

assetpath = Path(__file__).parent.parent / "Assets"

try:
    with open(f'{assetpath}/StyleSheets/scrollbar.qss', 'r') as qss_file:
        scrollbar_style = qss_file.read()
except:
    logger.error("Scrollbar Stylesheet not Found!")
    logger.warning("Returning empty String")
    scrollbar_style = ""
else:
    logger.info("Scrollbar Stylesheet loaded.")
