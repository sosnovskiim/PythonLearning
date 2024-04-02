from PyQt6 import QtWidgets
from PyQt6 import QtCore
import sys


class MyWindow(QtWidgets.QWidget):
    window_width, window_height = 400, 300
    button_width, button_height = 100, 20
    button_width_narrow = 50
    margin = 30
    margin_narrow = 15
    cnt_positive, cnt_negative = None, None

    def __init__(self):
        super().__init__()
        self.get_voices()

        self.setWindowTitle('Помощник в принятии решений')
        self.resize(self.window_width, self.window_height)

        self.label = QtWidgets.QLabel('Вы за или против?', self)
        self.label.adjustSize()
        self.label.move(
            (self.window_width - self.label.width()) // 2, self.margin
        )

        self.buttonPositive = QtWidgets.QPushButton('За', self)
        self.buttonPositive.resize(self.button_width_narrow, self.button_height)
        self.buttonPositive.move(
            self.window_width // 2 - self.button_width_narrow - self.margin_narrow, self.margin * 2
        )
        self.buttonPositive.clicked.connect(self.on_click_positive_or_negative)

        self.buttonNegative = QtWidgets.QPushButton('Против', self)
        self.buttonNegative.resize(self.button_width_narrow, self.button_height)
        self.buttonNegative.move(
            self.window_width // 2 + self.margin_narrow, self.margin * 2
        )
        self.buttonNegative.clicked.connect(self.on_click_positive_or_negative)

        self.labelPositive = QtWidgets.QLabel(f'Голосов за: {self.cnt_positive}', self)
        self.labelPositive.adjustSize()
        self.labelPositive.move(
            (self.window_width - self.labelPositive.width()) // 2, self.window_height // 2 - self.margin
        )

        self.labelNegative = QtWidgets.QLabel(f'Голосов против: {self.cnt_negative}', self)
        self.labelNegative.adjustSize()
        self.labelNegative.move(
            (self.window_width - self.labelNegative.width()) // 2, self.window_height // 2
        )

        self.buttonCount = QtWidgets.QPushButton('Сброс', self)
        self.buttonCount.resize(self.button_width, self.button_height)
        self.buttonCount.move(
            (self.window_width - self.button_width) // 2, self.window_height - self.margin * 2
        )
        self.buttonCount.clicked.connect(self.on_click_reset)

        #
        self.timeEvent = QtWidgets.QTimeEdit(self)
        self.timeEvent.clear()
        self.timeEvent.time()
        self.calendarEvent = QtWidgets.QCalendarWidget(self)
        self.calendarEvent.setSelectedDate(QtCore.QDate(2024, 3, 2))
        self.calendarEvent.selectedDate()

        self.show()

    def on_click_positive_or_negative(self):
        if self.sender() is self.buttonPositive:
            self.cnt_positive += 1
            self.set_voices()
            self.labelPositive.setText(f'Голосов за: {self.cnt_positive}')
            self.labelPositive.adjustSize()
        else:
            self.cnt_negative += 1
            self.set_voices()
            self.labelNegative.setText(f'Голосов против: {self.cnt_negative}')
            self.labelNegative.adjustSize()

    def on_click_reset(self):
        self.cnt_positive, self.cnt_negative = 0, 0
        self.set_voices()
        self.labelPositive.setText(f'Голосов за: {self.cnt_positive}')
        self.labelNegative.setText(f'Голосов против: {self.cnt_negative}')

    def get_voices(self):
        with open('voices.txt') as voices:
            self.cnt_positive = int(voices.readline()[10:])
            self.cnt_negative = int(voices.readline()[10:])

    def set_voices(self):
        with open('voices.txt', 'w') as voices:
            voices.write(f'positive: {self.cnt_positive}\nnegative: {self.cnt_negative}')


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())
