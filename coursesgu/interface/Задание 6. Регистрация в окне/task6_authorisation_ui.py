# Form implementation generated from reading ui file 'task6_authorisation.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AuthorisationForm(object):
    def setupUi(self, AuthorisationForm):
        AuthorisationForm.setObjectName("AuthorisationForm")
        AuthorisationForm.resize(480, 640)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_title = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_title.setContentsMargins(0, 0, 0, 0)
        self.layout_title.setObjectName("layout_title")
        self.label_title = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.layout_title.addWidget(self.label_title)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 481, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_input = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_input.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_input.setContentsMargins(80, 0, 80, 0)
        self.layout_input.setSpacing(6)
        self.layout_input.setObjectName("layout_input")
        self.input_login = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_login.setFont(font)
        self.input_login.setText("")
        self.input_login.setMaxLength(32)
        self.input_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.input_login.setObjectName("input_login")
        self.layout_input.addWidget(self.input_login)
        self.input_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_password.setFont(font)
        self.input_password.setMaxLength(32)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.input_password.setObjectName("input_password")
        self.layout_input.addWidget(self.input_password)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 200, 481, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layout_sign_in = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_sign_in.setContentsMargins(80, 0, 80, 0)
        self.layout_sign_in.setSpacing(6)
        self.layout_sign_in.setObjectName("layout_sign_in")
        self.button_sign_in = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_sign_in.setFont(font)
        self.button_sign_in.setObjectName("button_sign_in")
        self.layout_sign_in.addWidget(self.button_sign_in)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 260, 481, 21))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layout_error = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_error.setContentsMargins(0, 0, 0, 0)
        self.layout_error.setObjectName("layout_error")
        self.label_error = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.layout_error.addWidget(self.label_error)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 560, 481, 21))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.layout_note = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_note.setContentsMargins(0, 0, 0, 0)
        self.layout_note.setObjectName("layout_note")
        self.label_note = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_note.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_note.setObjectName("label_note")
        self.layout_note.addWidget(self.label_note)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=AuthorisationForm)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 580, 481, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.layout_sign_up = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.layout_sign_up.setContentsMargins(80, 0, 80, 0)
        self.layout_sign_up.setObjectName("layout_sign_up")
        self.button_sign_up = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_sign_up.setFont(font)
        self.button_sign_up.setObjectName("button_sign_up")
        self.layout_sign_up.addWidget(self.button_sign_up)

        self.retranslateUi(AuthorisationForm)
        QtCore.QMetaObject.connectSlotsByName(AuthorisationForm)

    def retranslateUi(self, AuthorisationForm):
        _translate = QtCore.QCoreApplication.translate
        AuthorisationForm.setWindowTitle(_translate("AuthorisationForm", "Авторизация"))
        self.label_title.setText(_translate("AuthorisationForm", "Авторизация пользователя"))
        self.input_login.setPlaceholderText(_translate("AuthorisationForm", "Логин"))
        self.input_password.setPlaceholderText(_translate("AuthorisationForm", "Пароль"))
        self.button_sign_in.setText(_translate("AuthorisationForm", "Войти"))
        self.label_error.setText(_translate("AuthorisationForm", "Неверные данные, попробуйте ещё раз."))
        self.label_note.setText(_translate("AuthorisationForm", "Нет аккаунта?"))
        self.button_sign_up.setText(_translate("AuthorisationForm", "Создать аккаунт"))
