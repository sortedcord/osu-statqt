from loguru import logger

# Scrollbar
try:
    with open('Components/scrollbar.qss', 'r') as qss_file:
        scrollbar_style = qss_file.read()
except:
    logger.error("Scrollbar Stylesheet not Found!")
    logger.warning("Returning empty String")
    scrollbar_style = ""
else:
    logger.info("Scrollbar Stylesheet loaded.")
