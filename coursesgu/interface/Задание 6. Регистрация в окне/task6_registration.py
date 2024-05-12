import hashlib
import json
import re
from string import (
    whitespace,
    ascii_lowercase,
    ascii_uppercase,
    ascii_letters,
    digits,
    punctuation,
)
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QMessageBox,
)
from task6_registration_ui import Ui_RegistrationForm


class RegistrationWidget(QDialog, Ui_RegistrationForm):
    file_name: str = 'users.json'
    users: list[dict[str, str]]
    key_login: str = 'login'
    key_password: str = 'password'
    key_email: str = 'email'
    key_phone: str = 'phone'
    key_surname: str = 'surname'
    key_name: str = 'name'
    key_patronymic: str = 'patronymic'
    is_valid_login: bool = False
    is_valid_password: bool = False
    is_valid_password_repeat: bool = False
    is_valid_email: bool = False
    is_valid_phone: bool = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_users()
        self.input_login.textEdited.connect(self.on_edited_login)
        self.input_password.textEdited.connect(self.on_edited_password)
        self.input_password_repeat.textEdited.connect(self.on_edited_password_repeat)
        self.input_email.textEdited.connect(self.on_edited_email)
        self.input_phone.textEdited.connect(self.on_edited_phone)
        self.button_info_login.clicked.connect(self.on_click_info_login)
        self.button_info_password.clicked.connect(self.on_click_info_password)
        self.button_sign_up.clicked.connect(self.on_click_sign_up)

    def on_edited_login(self, chars: str):
        if not chars:
            self.hint_login.setText(
                'Введите логин.'
            )
        elif any(c in whitespace for c in chars):
            self.hint_login.setText(
                'Поле не может содержать пробельные символы.'
            )
        elif len(chars) < 5:
            self.hint_login.setText(
                'Логин должен состоять не менее чем из 5 символов.'
            )
        elif any(c not in ascii_letters + digits for c in chars):
            self.hint_login.setText(
                'Логин может включать только буквы и цифры.'
            )
        elif any(user[self.key_login] == chars for user in self.users):
            self.hint_login.setText(
                'Пользователь с таким логином уже существует.'
            )
        else:
            self.hint_login.setText(
                'Логин в порядке.'
            )
            self.update_edited_data(hint=self.hint_login, is_valid=True)
            return
        self.update_edited_data(hint=self.hint_login, is_valid=False)

    def on_edited_password(self, chars: str):
        if not chars:
            self.hint_password.setText(
                'Введите пароль.'
            )
        elif any(c in whitespace for c in chars):
            self.hint_password.setText(
                'Поле не может содержать пробельные символы.'
            )
        elif len(chars) < 8:
            self.hint_password.setText(
                'Пароль должен состоять не менее чем из 8 символов.'
            )
        elif any(c not in ascii_letters + digits + punctuation for c in chars):
            self.hint_password.setText(
                'Пароль может включать только буквы, цифры и спец. символы.'
            )
        elif not any(c in ascii_lowercase for c in chars):
            self.hint_password.setText(
                'Пароль должен включать хотя бы одну строчную букву.'
            )
        elif not any(c in ascii_uppercase for c in chars):
            self.hint_password.setText(
                'Пароль должен включать хотя бы одну прописную букву.'
            )
        elif not any(c in digits for c in chars):
            self.hint_password.setText(
                'Пароль должен включать хотя бы одну цифру.'
            )
        elif not any(c in punctuation for c in chars):
            self.hint_password.setText(
                'Пароль должен включать хотя бы один спец. символ.'
            )
        else:
            self.hint_password.setText(
                'Пароль в порядке.'
            )
            self.update_edited_data(hint=self.hint_password, is_valid=True)
            return
        self.update_edited_data(hint=self.hint_password, is_valid=False)

    def on_edited_password_repeat(self, chars: str):
        if not chars:
            self.hint_password_repeat.setText(
                'Повторите пароль.'
            )
        elif self.input_password.text() != chars:
            self.hint_password_repeat.setText(
                'Пароли не совпадают.'
            )
        else:
            self.hint_password_repeat.setText(
                'Пароли совпадают.'
            )
            self.update_edited_data(hint=self.hint_password_repeat, is_valid=True)
            return
        self.update_edited_data(hint=self.hint_password_repeat, is_valid=False)

    def on_edited_email(self, chars: str):
        if not chars:
            self.hint_email.setText(
                'Введите адрес электронной почты.'
            )
        elif any(c in whitespace for c in chars):
            self.hint_email.setText(
                'Поле не может содержать пробельные символы.'
            )
        elif not re.match(r'.+@.+\..+', chars):
            self.hint_email.setText(
                'Поле не соответствует формату адреса электронной почты.'
            )
        elif any(user[self.key_email] == chars for user in self.users):
            self.hint_email.setText(
                'Пользователь с таким адресом уже существует.'
            )
        else:
            self.hint_email.setText(
                'Адрес электронной почты в порядке.'
            )
            self.update_edited_data(hint=self.hint_email, is_valid=True)
            return
        self.update_edited_data(hint=self.hint_email, is_valid=False)

    def on_edited_phone(self, chars: str):
        if not re.match(r'\+7 \(\d\d\d\) \d\d\d-\d\d-\d\d', chars):
            self.hint_phone.setText(
                'Введите номер телефона.'
            )
        elif any(user[self.key_phone] == chars for user in self.users):
            self.hint_phone.setText(
                'Пользователь с таким номером уже существует.'
            )
        else:
            self.hint_phone.setText(
                'Номер телефона в порядке.'
            )
            self.update_edited_data(hint=self.hint_phone, is_valid=True)
            return
        self.update_edited_data(hint=self.hint_phone, is_valid=False)

    def update_edited_data(self, hint: QLabel, is_valid: bool):
        if hint is self.hint_login:
            self.is_valid_login = is_valid
        elif hint is self.hint_password:
            self.is_valid_password = is_valid
        elif hint is self.hint_password_repeat:
            self.is_valid_password_repeat = is_valid
        elif hint is self.hint_email:
            self.is_valid_email = is_valid
        elif hint is self.hint_phone:
            self.is_valid_phone = is_valid
        self.button_sign_up.setEnabled(
            self.is_valid_login and self.is_valid_password and
            self.is_valid_password_repeat and self.is_valid_email and self.is_valid_phone
        )

    def on_click_info_login(self):
        self.show_message(button=self.button_info_login)

    def on_click_info_password(self):
        self.show_message(button=self.button_info_password)

    def on_click_sign_up(self):
        self.add_user()
        self.show_message(button=self.button_sign_up)

    def show_message(self, button: QPushButton):
        if button is self.button_info_login:
            title: str = 'Требования к логину'
            text: str = (
                'Логин должен состоять не менее чем из 5 символов.\n'
                'Может включать только латинские буквы и цифры.'
            )
        elif button is self.button_info_password:
            title: str = 'Требования к паролю'
            text: str = (
                'Пароль должен состоять не менее чем из 8 символов.\n'
                'Должен включать хотя бы по одной латинской строчной и прописной букве,\n'
                'хотя бы одну цифру и хотя бы один спец. символ.'
            )
        else:
            title: str = 'Регистрация'
            text: str = f'Вы успешно зарегистрированы, {self.input_login.text()}'
        dialog = QMessageBox(self)
        dialog.setWindowTitle(title)
        dialog.setText(text)
        if dialog.exec() == QMessageBox.StandardButton.Ok and button is self.button_sign_up:
            self.close()

    def get_users(self):
        with open(self.file_name, 'r', encoding='utf-8') as file_in:
            self.users: list[dict[str, str]] = json.load(file_in)

    def add_user(self):
        hashed_password = hashlib.md5(self.input_password.text().encode()).hexdigest()
        self.users.append({
            self.key_login: self.input_login.text(),
            self.key_password: hashed_password,
            self.key_email: self.input_email.text(),
            self.key_phone: self.input_phone.text(),
            self.key_surname: self.input_surname.text(),
            self.key_name: self.input_name.text(),
            self.key_patronymic: self.input_patronymic.text(),
        })
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.users, file_out, ensure_ascii=False, indent=4)
