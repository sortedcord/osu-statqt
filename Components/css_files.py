# Scrollbar
try:
    with open('Components/scrollbar.qss', 'r') as qss_file:
        scrollbar_style = qss_file.read()
except:
    print("Requested file not found")
    scrollbar_style = ""
