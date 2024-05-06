import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from part3_ui import Ui_Form


class DecisionAssistantWidget(QWidget, Ui_Form):
    questions: list[dict] = []
    current_question: int = -1
    file_name: str = 'questions.json'
    question_name: str = 'question_name'
    positive_arguments: str = 'positive_arguments'
    negative_arguments: str = 'negative_arguments'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_question_add.clicked.connect(self.on_click_question_add)
        self.button_question_delete.clicked.connect(self.on_click_question_delete)
        self.combo_box_question.currentIndexChanged.connect(self.on_changed_question)
        self.button_argument_add_positive.clicked.connect(self.on_click_argument_add)
        self.button_argument_add_negative.clicked.connect(self.on_click_argument_add)
        self.button_argument_move_up.clicked.connect(self.on_click_argument_move)
        self.button_argument_move_down.clicked.connect(self.on_click_argument_move)
        self.get_questions()
        self.update_on_start()

    def on_click_question_add(self):
        questions: list[str] = [q[self.question_name] for q in self.questions]
        question: str = self.edit_question.text()
        if question and question not in self.questions:
            self.add_question(question=question)
            self.update_on_question_add(question=question)

    def on_click_question_delete(self):
        self.delete_question()
        self.update_on_question_delete()

    def on_changed_question(self, index):
        self.current_question = index

    def on_click_argument_add(self):
        argument: str = self.edit_argument.text()
        if self.sender() is self.button_argument_add_positive:
            arguments: list[str] = self.questions[self.current_question][self.positive_arguments]
            if argument and argument not in arguments:
                self.add_argument(argument=argument, is_positive=True)
                self.update_on_argument_add(argument=argument, is_positive=True)
        else:
            arguments: list[str] = self.questions[self.current_question][self.negative_arguments]
            if argument and argument not in arguments:
                self.add_argument(argument=argument, is_positive=False)
                self.update_on_argument_add(argument=argument, is_positive=False)

    def on_click_argument_move(self):
        pass

    def get_questions(self):
        with open(self.file_name, 'r', encoding='utf-8') as file_in:
            self.questions: list[dict] = json.load(file_in)

    def add_question(self, question: str):
        self.questions.append({
            self.question_name: question,
            self.positive_arguments: [],
            self.negative_arguments: [],
        })
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def delete_question(self):
        self.questions.pop(self.current_question)
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def add_argument(self, argument: str, is_positive: bool):
        if is_positive:
            self.questions[self.current_question][self.positive_arguments].append(argument)
        else:
            self.questions[self.current_question][self.negative_arguments].append(argument)
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def update_on_start(self):
        if len(self.questions) > 0:
            self.update_on_questions_is_not_empty()
            questions: list[str] = [q[self.question_name] for q in self.questions]
            self.combo_box_question.addItems(questions)
            self.combo_box_question.setCurrentText(self.questions[self.current_question][self.question_name])


    def update_on_question_add(self, question: str):
        if len(self.questions) == 1:
            self.update_on_questions_is_not_empty()
        self.edit_question.clear()
        self.combo_box_question.addItem(question)
        self.combo_box_question.setCurrentText(question)
        self.current_question = len(self.questions) - 1

    def update_on_question_delete(self):
        if len(self.questions) == 0:
            self.update_on_questions_is_empty()
        self.edit_question.clear()
        self.combo_box_question.removeItem(self.current_question)
        self.current_question = len(self.questions) - 1

    def update_on_questions_is_not_empty(self):
        self.button_question_delete.setEnabled(True)
        self.combo_box_question.setEnabled(True)
        self.edit_argument.setEnabled(True)
        self.button_argument_add_positive.setEnabled(True)
        self.button_argument_add_negative.setEnabled(True)

    def update_on_questions_is_empty(self):
        self.button_question_delete.setEnabled(False)
        self.combo_box_question.setEnabled(False)
        self.edit_argument.setEnabled(False)
        self.button_argument_add_positive.setEnabled(False)
        self.button_argument_add_negative.setEnabled(False)

    def update_on_argument_add(self, argument: str, is_positive: bool):
        self.edit_argument.clear()
        if is_positive:
            self.list_argument_positive.addItem(argument)
            self.number_argument_positive.display(len(self.questions[self.current_question][self.positive_arguments]))
        else:
            self.list_argument_negative.addItem(argument)
            self.number_argument_negative.display(len(self.questions[self.current_question][self.negative_arguments]))

    def update_on_argument_move(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DecisionAssistantWidget()
    ex.show()
    sys.exit(app.exec())
