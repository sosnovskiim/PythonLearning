from PyQt6 import QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    window_width, window_height = 400, 300
    button_width, button_height = 100, 20
    button_width_narrow = 50
    margin = 30
    shift = 10
    click_count = 0

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Studying PyQt')
        self.resize(self.window_width, self.window_height)

        self.label = QtWidgets.QLabel('Какой-то текст...', self)
        self.label.adjustSize()
        self.label.move(
            (self.window_width - self.label.width()) // 2, self.margin
        )

        self.buttonMove = QtWidgets.QPushButton('Двигать', self)
        self.buttonMove.resize(self.button_width, self.button_height)
        self.buttonMove.move(
            (self.window_width - self.button_width) // 2, (self.window_height - self.button_height) // 2
        )
        self.buttonMove.clicked.connect(self.on_click_move)

        self.buttonCount = QtWidgets.QPushButton('Считать', self)
        self.buttonCount.resize(self.button_width, self.button_height)
        self.buttonCount.move(
            (self.window_width - self.button_width) // 2, (self.window_height - self.button_height) // 2 + self.margin
        )
        self.buttonCount.clicked.connect(self.on_click_count)

        self.labelCount = QtWidgets.QLabel(':(', self)
        self.labelCount.adjustSize()
        self.labelCount.move(
            (self.window_width - self.labelCount.width()) // 2, self.window_height // 2 + self.margin * 2
        )

        self.buttonYes = QtWidgets.QPushButton('Да', self)
        self.buttonYes.resize(self.button_width_narrow, self.button_height)
        self.buttonYes.move(
            self.margin, self.window_height - self.margin
        )
        self.buttonYes.clicked.connect(self.on_click_yes_or_no)

        self.buttonNo = QtWidgets.QPushButton('Нет', self)
        self.buttonNo.resize(self.button_width_narrow, self.button_height)
        self.buttonNo.move(
            self.window_width - self.button_width_narrow - 30, self.window_height - self.margin
        )
        self.buttonNo.clicked.connect(self.on_click_yes_or_no)

        self.labelYesOrNo = QtWidgets.QLabel('Да или нет?', self)
        self.labelYesOrNo.adjustSize()
        self.labelYesOrNo.move(
            (self.window_width - self.labelYesOrNo.width()) // 2, self.window_height - self.margin
        )

        self.show()

    def on_click_move(self):
        if self.buttonMove.x() != self.window_width - self.button_width:
            self.buttonMove.move(
                self.buttonMove.x() + self.shift, (self.window_height - self.button_height) // 2
            )
        else:
            self.buttonMove.move(0, (self.window_height - self.button_height) // 2)

    def on_click_count(self):
        self.click_count += 1
        self.labelCount.setText(f'Кнопку нажали {self.click_count} раз')
        self.labelCount.adjustSize()
        self.labelCount.move(
            (self.window_width - self.labelCount.width()) // 2, self.window_height // 2 + self.margin * 2
        )

    def on_click_yes_or_no(self):
        if self.sender() is self.buttonYes:
            self.labelYesOrNo.setText('Да!')
        else:
            self.labelYesOrNo.setText('Нет!')
        self.labelYesOrNo.adjustSize()
        self.labelYesOrNo.move(
            (self.window_width - self.labelYesOrNo.width()) // 2, self.window_height - self.margin
        )


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())
