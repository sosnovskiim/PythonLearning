from PyQt6.QtWidgets import QWidget
from task6_application_ui import Ui_ApplicationForm


class ApplicationWidget(QWidget, Ui_ApplicationForm):
    current_user: dict[str, str]
    key_login: str = 'login'

    def __init__(self, current_user: dict[str, str]):
        super().__init__()
        self.setupUi(self)
        self.current_user = current_user
        self.label_login.setText(self.current_user[self.key_login])
