# Form implementation generated from reading ui file 'task7_form.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.line_edit = QtWidgets.QLineEdit(parent=Form)
        self.line_edit.setGeometry(QtCore.QRect(20, 440, 600, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_edit.setFont(font)
        self.line_edit.setObjectName("line_edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.line_edit.setPlaceholderText(_translate("Form", "Двойное нажатие мыши добавляет новые клавиши."))
