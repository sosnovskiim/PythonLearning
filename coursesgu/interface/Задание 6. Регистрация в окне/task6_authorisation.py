import hashlib
import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from task6_authorisation_ui import Ui_AuthorisationForm
from task6_application import ApplicationWidget
from task6_registration import RegistrationWidget


class AuthorisationWidget(QWidget, Ui_AuthorisationForm):
    file_name: str = 'users.json'
    users: list[dict[str, str]]
    key_login: str = 'login'
    key_password: str = 'password'
    current_user: dict[str, str]
    application_widget: ApplicationWidget
    registration_widget: RegistrationWidget

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_error.hide()
        self.button_sign_in.clicked.connect(self.on_click_sign_in)
        self.button_sign_up.clicked.connect(self.on_click_sign_up)

    def on_click_sign_in(self):
        self.get_users()
        for user in self.users:
            if user[self.key_login] == self.input_login.text():
                self.current_user: dict[str, str] = user
                break
        else:
            self.current_user = dict()
        hashed_password = hashlib.md5(self.input_password.text().encode()).hexdigest()
        if self.current_user and hashed_password == self.current_user[self.key_password]:
            self.application_widget = ApplicationWidget(current_user=self.current_user)
            self.application_widget.show()
            self.close()
        else:
            self.label_error.show()

    def on_click_sign_up(self):
        self.registration_widget = RegistrationWidget()
        self.registration_widget.exec()

    def get_users(self):
        with open(self.file_name, 'r', encoding='utf-8') as file_in:
            self.users: list[dict[str, str]] = json.load(file_in)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthorisationWidget()
    ex.show()
    sys.exit(app.exec())
