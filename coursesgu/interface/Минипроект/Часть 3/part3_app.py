import sys
from PyQt6.QtWidgets import QApplication, QWidget
from part3_ui import Ui_Form


class DecisionAssistant(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_after_restart()
        self.button_ask.clicked.connect(self.on_click_ask)
        self.button_positive.clicked.connect(self.on_click_voice)
        self.button_negative.clicked.connect(self.on_click_voice)
        self.button_move_up.clicked.connect(self.on_click_move)
        self.button_move_down.clicked.connect(self.on_click_move)
        self.button_reset.clicked.connect(self.on_click_reset)

    def on_click_ask(self):
        if self.edit_question.text():
            self.question = self.edit_question.text()
            add_question_to_file(self.question)
            self.update_after_question()

    def on_click_voice(self):
        if self.sender() is self.button_positive:
            argument = self.edit_argument.text()
            self.positive_voices.append(argument)
            add_positive_voice_to_file(argument)
            self.update_after_positive_voice(argument)
        else:
            argument = self.edit_argument.text()
            self.negative_voices.append(argument)
            add_negative_voice_to_file(argument)
            self.update_after_negative_voice(argument)
        self.edit_argument.clear()

    def on_click_move(self):
        pass

    def on_click_reset(self):
        self.question = 'Пока нет вопроса'
        self.positive_voices.clear()
        self.negative_voices.clear()
        clear_voices()
        self.update_after_reset()

    def update_after_restart(self):
        if self.question != 'Пока нет вопроса':
            self.update_after_question()
            self.list_positive.addItems(self.positive_voices)
            self.list_negative.addItems(self.negative_voices)
            self.label_positive.setText(f'Голосов: {len(self.positive_voices)}')
            self.label_negative.setText(f'Голосов: {len(self.negative_voices)}')

    def update_after_question(self):
        self.label_question.setText(self.question)
        self.edit_argument.setEnabled(True)
        self.button_positive.setEnabled(True)
        self.button_negative.setEnabled(True)
        self.edit_question.clear()
        self.edit_question.setEnabled(False)
        self.button_ask.setEnabled(False)

    def update_after_positive_voice(self, argument):
        self.list_positive.addItem(argument)
        self.label_positive.setText(f'Голосов: {len(self.positive_voices)}')

    def update_after_negative_voice(self, argument):
        self.list_negative.addItem(argument)
        self.label_negative.setText(f'Голосов: {len(self.negative_voices)}')

    def update_after_reset(self):
        self.label_question.setText(self.question)
        self.edit_argument.clear()
        self.edit_argument.setEnabled(False)
        self.button_positive.setEnabled(False)
        self.button_negative.setEnabled(False)
        self.label_positive.setText('Голосов: нет')
        self.label_negative.setText('Голосов: нет')
        self.list_positive.clear()
        self.list_negative.clear()
        self.edit_question.setEnabled(True)
        self.button_ask.setEnabled(True)


def get_question():
    with open('question.txt') as f:
        temp = f.read()
        if temp:
            return temp
        return 'Пока нет вопроса'


def get_positive_voices():
    with open('positive.txt') as f:
        temp = f.read().split('\n')
        if len(temp) > 1:
            return temp[1:]
        return list()


def get_negative_voices():
    with open('negative.txt') as f:
        temp = f.read().split('\n')
        if len(temp) > 1:
            return temp[1:]
        return list()


def add_question_to_file(question):
    with open('question.txt', 'w') as f:
        f.write(question)


def add_positive_voice_to_file(voice):
    with open('positive.txt', 'a') as f:
        f.write('\n')
        f.write(voice)


def add_negative_voice_to_file(voice):
    with open('negative.txt', 'a') as f:
        f.write('\n')
        f.write(voice)


def clear_voices():
    with open('question.txt', 'w') as f:
        f.write('')
    with open('positive.txt', 'w') as f:
        f.write('')
    with open('negative.txt', 'w') as f:
        f.write('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DecisionAssistant()
    ex.show()
    sys.exit(app.exec())
