import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QListWidgetItem
from part3_ui import Ui_Form


# кнопки перемещения аргументов enabled при смене вопроса при выделенном аргументе
class DecisionAssistantWidget(QWidget, Ui_Form):
    questions: list[dict]
    current_question: int
    current_argument: int
    is_current_list_positive: bool
    file_name: str = 'questions.json'
    question_name: str = 'question_name'
    arguments_positive: str = 'arguments_positive'
    arguments_negative: str = 'arguments_negative'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_question_add.clicked.connect(self.on_click_question_add)
        self.button_question_delete.clicked.connect(self.on_click_question_delete)
        self.combo_box_question.currentIndexChanged.connect(self.on_changed_question)
        self.button_argument_add_positive.clicked.connect(self.on_click_argument_add)
        self.button_argument_add_negative.clicked.connect(self.on_click_argument_add)
        self.list_arguments_positive.currentRowChanged.connect(self.on_changed_argument)
        self.list_arguments_negative.currentRowChanged.connect(self.on_changed_argument)
        self.button_argument_move_up.clicked.connect(self.on_click_argument_move)
        self.button_argument_move_down.clicked.connect(self.on_click_argument_move)
        self.get_questions()
        self.update_on_start()

    def on_click_question_add(self):
        questions: list[str] = [q[self.question_name] for q in self.questions]
        question: str = self.edit_question.text()
        if question and question not in questions:
            self.add_question(question=question)
            self.update_on_question_add(question=question)

    def on_click_question_delete(self):
        self.delete_question()
        self.update_on_question_delete()

    def on_changed_question(self, index: int):
        if len(self.questions) == 0:
            self.current_question = -1
            self.list_arguments_positive.clear()
            self.list_arguments_negative.clear()
            self.number_arguments_positive.display(0)
            self.number_arguments_negative.display(0)
        else:
            self.current_question = index
            self.update_on_question_changed()

    def on_click_argument_add(self):
        argument: str = self.edit_argument.text()
        if self.sender() is self.button_argument_add_positive:
            arguments: list[str] = self.questions[self.current_question][self.arguments_positive]
            if argument and argument not in arguments:
                self.add_argument(argument=argument, is_positive=True)
                self.update_on_argument_add(argument=argument, is_positive=True)
        else:
            arguments: list[str] = self.questions[self.current_question][self.arguments_negative]
            if argument and argument not in arguments:
                self.add_argument(argument=argument, is_positive=False)
                self.update_on_argument_add(argument=argument, is_positive=False)

    def on_changed_argument(self, index: int):
        self.current_argument = index
        if self.sender() is self.list_arguments_positive:
            self.is_current_list_positive = True
            self.update_on_argument_changed(index=index, is_positive=True)
        else:
            self.is_current_list_positive = False
            self.update_on_argument_changed(index=index, is_positive=False)

    def on_click_argument_move(self):
        if self.sender() is self.button_argument_move_up:
            self.move_argument(index=self.current_argument, is_positive=self.is_current_list_positive, is_up=True)
            self.update_on_argument_move()
        else:
            self.move_argument(index=self.current_argument, is_positive=self.is_current_list_positive, is_up=False)
            self.update_on_argument_move()

    def get_questions(self):
        with open(self.file_name, 'r', encoding='utf-8') as file_in:
            self.questions: list[dict] = json.load(file_in)

    def add_question(self, question: str):
        self.questions.append({
            self.question_name: question,
            self.arguments_positive: [],
            self.arguments_negative: [],
        })
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def delete_question(self):
        self.questions.pop(self.current_question)
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def add_argument(self, argument: str, is_positive: bool):
        if is_positive:
            self.questions[self.current_question][self.arguments_positive].append(argument)
        else:
            self.questions[self.current_question][self.arguments_negative].append(argument)
        with open(self.file_name, 'w', encoding='utf-8') as file_out:
            json.dump(self.questions, file_out, ensure_ascii=False, indent=4)

    def move_argument(self, index: int, is_positive: bool, is_up: bool):
        pass

    def update_on_start(self):
        if len(self.questions) > 0:
            self.update_on_questions_is_not_empty()
            questions: list[str] = [q[self.question_name] for q in self.questions]
            self.combo_box_question.addItems(questions)
            self.combo_box_question.setCurrentText(self.questions[self.current_question][self.question_name])
            self.update_on_question_changed()

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
        self.list_arguments_positive.setEnabled(True)
        self.list_arguments_negative.setEnabled(True)

    def update_on_questions_is_empty(self):
        self.button_question_delete.setEnabled(False)
        self.combo_box_question.setEnabled(False)
        self.edit_argument.setEnabled(False)
        self.button_argument_add_positive.setEnabled(False)
        self.button_argument_add_negative.setEnabled(False)
        self.list_arguments_positive.setEnabled(False)
        self.list_arguments_negative.setEnabled(False)

    def update_on_question_changed(self):
        arguments_positive: list[str] = self.questions[self.current_question][self.arguments_positive]
        arguments_negative: list[str] = self.questions[self.current_question][self.arguments_negative]
        self.list_arguments_positive.clear()
        self.list_arguments_negative.clear()
        self.list_arguments_positive.addItems(arguments_positive)
        self.list_arguments_negative.addItems(arguments_negative)
        self.number_arguments_positive.display(len(arguments_positive))
        self.number_arguments_negative.display(len(arguments_negative))

    def update_on_argument_add(self, argument: str, is_positive: bool):
        self.edit_argument.clear()
        if is_positive:
            self.list_arguments_positive.addItem(argument)
            self.number_arguments_positive.display(len(self.questions[self.current_question][self.arguments_positive]))
        else:
            self.list_arguments_negative.addItem(argument)
            self.number_arguments_negative.display(len(self.questions[self.current_question][self.arguments_negative]))

    def update_on_argument_changed(self, index: int, is_positive: bool):
        if index == 0:
            self.button_argument_move_up.setEnabled(False)
        else:
            self.button_argument_move_up.setEnabled(True)
        if is_positive:
            arguments: list[str] = self.questions[self.current_question][self.arguments_positive]
        else:
            arguments: list[str] = self.questions[self.current_question][self.arguments_negative]
        if index == len(arguments) - 1:
            self.button_argument_move_down.setEnabled(False)
        else:
            self.button_argument_move_down.setEnabled(True)

    def update_on_argument_move(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DecisionAssistantWidget()
    ex.show()
    sys.exit(app.exec())
