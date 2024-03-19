import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class DecisionAssistant(QMainWindow):
    question = 'Пока нет вопроса'
    positive_voices = list()
    negative_voices = list()

    def __init__(self):
        super().__init__()
        uic.loadUi('part2.ui', self)
        self.get_voices()
        self.label_question.setText(self.question)
        self.list_positive.addItems(self.positive_voices)
        self.list_negative.addItems(self.negative_voices)

        self.button_ask.clicked.connect(self.on_click_ask)
        self.button_positive.clicked.connect(self.on_click_positive_or_negative)
        self.button_negative.clicked.connect(self.on_click_positive_or_negative)
        self.button_reset.clicked.connect(self.on_click_reset)

    def on_click_ask(self):
        if self.edit_question.text():
            self.question = self.edit_question.text()
            self.label_question.setText(self.question)
            self.edit_argument.setEnabled(True)
            self.button_positive.setEnabled(True)
            self.button_negative.setEnabled(True)
            self.edit_question.clear()
            self.edit_question.setEnabled(False)
            self.button_ask.setEnabled(False)

    def on_click_positive_or_negative(self):
        if self.sender() is self.button_positive:
            argument = self.edit_argument.text()
            self.list_positive.addItem(argument)
            self.positive_voices.append(argument)
            self.add_positive()
            self.label_positive.setText(f'Голосов: {len(self.positive_voices)}')
            self.edit_argument.clear()
        else:
            argument = self.edit_argument.text()
            self.list_negative.addItem(argument)
            self.negative_voices.append(argument)
            self.add_negative()
            self.label_negative.setText(f'Голосов: {len(self.negative_voices)}')
            self.edit_argument.clear()

    def on_click_reset(self):
        self.question = 'Пока нет вопроса'
        self.label_question.setText(self.question)
        self.edit_argument.clear()
        self.edit_argument.setEnabled(False)
        self.button_positive.setEnabled(False)
        self.button_negative.setEnabled(False)
        self.label_positive.setText('Голосов: нет')
        self.label_negative.setText('Голосов: нет')
        self.list_positive.clear()
        self.list_negative.clear()
        self.positive_voices.clear()
        self.negative_voices.clear()
        self.reset_voices()
        self.edit_question.setEnabled(True)
        self.button_ask.setEnabled(True)

    def get_voices(self):
        with open('question.txt') as f:
            temp = f.read()
            if temp:
                self.question = temp
        with open('positive.txt') as f:
            self.positive_voices = f.read().split('\n')
        with open('negative.txt') as f:
            self.negative_voices = f.read().split('\n')

    def add_positive(self):
        with open('positive.txt', 'w') as f:
            f.writelines(self.positive_voices)

    def add_negative(self):
        with open('negative.txt', 'w') as f:
            f.writelines(self.negative_voices)

    def reset_voices(self):
        with open('question.txt', 'w') as f:
            f.write('')
        with open('positive.txt', 'w') as f:
            f.write('')
        with open('negative.txt', 'w') as f:
            f.write('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DecisionAssistant()
    widget.show()
    sys.exit(app.exec())
