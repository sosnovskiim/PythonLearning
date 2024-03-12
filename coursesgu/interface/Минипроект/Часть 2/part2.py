import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class DecisionAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('part2.ui', self)
        self.get_voices()

        self.button_ask.clicked.connect(self.on_click_ask)
        self.button_positive.clicked.connect(self.on_click_positive_or_negative)
        self.button_negative.clicked.connect(self.on_click_positive_or_negative)
        self.button_reset.clicked.connect(self.on_click_reset)

    def on_click_ask(self):
        pass

    def on_click_positive_or_negative(self):
        pass

    def on_click_reset(self):
        pass

    def get_voices(self):
        pass

    def set_voices(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DecisionAssistant()
    widget.show()
    sys.exit(app.exec())
