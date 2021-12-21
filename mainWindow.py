import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QGroupBox,
                             QVBoxLayout, QHBoxLayout, QApplication,
                             QSizePolicy, QLineEdit, QCheckBox, QTabWidget)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        api_groupBox = QGroupBox()
        api_groupBox.setTitle("API")
        api_groupBox_layout = QHBoxLayout()
        api_groupBox.setLayout(api_groupBox_layout)

        get_api = QPushButton("GET API")

        client_id = QLineEdit()
        client_id.setPlaceholderText("Enter Client ID")

        client_secret = QLineEdit()
        client_secret.setPlaceholderText("Enter Client Secret")

        submit_api = QPushButton("SUBMIT")

        api_groupBox_layout.addWidget(get_api)
        api_groupBox_layout.addWidget(client_id)
        api_groupBox_layout.addWidget(client_secret)
        api_groupBox_layout.addWidget(submit_api)

        user_groupBox = QGroupBox()
        user_groupBox.setTitle("USER")
        user_groupBox_layout = QHBoxLayout()
        user_groupBox.setLayout(user_groupBox_layout)

        username_field = QLineEdit()
        username_field.setPlaceholderText("Enter Username / User ID")

        set_default_check = QCheckBox()
        set_default_check.setText("SET DEFAULT")

        submit_username = QPushButton("SUBMIT")

        user_groupBox_layout.addWidget(username_field)
        user_groupBox_layout.addWidget(set_default_check)
        user_groupBox_layout.addWidget(submit_username)

        tabs = QTabWidget()

        vbox = QVBoxLayout()
        vbox.addWidget(api_groupBox)
        vbox.addWidget(user_groupBox)
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 768, 743)
        self.setWindowTitle('Osu!StatQt 0.0.1')
        self.setStyleSheet("""
            background:rgb(42, 34, 38);
            color:rgb(255,255,255);
            """)
        self.show()


def main():
    app = QApplication(sys.argv)
    e = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
