import sys

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QPushButton
from task7_form import Ui_Form
from task7_dialog import Ui_Dialog


class KeypadForm(QWidget, Ui_Form):
    symbols: list[str] = []
    button_index: int = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        dialog = KeypadDialog(symbols=self.symbols)
        if dialog.exec():
            symbol = dialog.line_edit.text()
            self.symbols.append(symbol)
            button = QPushButton(text=symbol, parent=self)
            button.clicked.connect(self.on_click)
            button.setGeometry(QRect(event.pos().x(), event.pos().y(), 40, 40))
            font = QFont()
            font.setPointSize(12)
            button.setFont(font)
            button.setObjectName(f'button{self.button_index}')
            button.show()

    def on_click(self):
        self.line_edit.setText(self.line_edit.text() + self.sender().text())


class KeypadDialog(QDialog, Ui_Dialog):
    def __init__(self, symbols: list[str]):
        super().__init__()
        self.setupUi(self)
        self.symbols = symbols

    def accept(self):
        symbol = self.line_edit.text()
        if symbol and symbol not in self.symbols:
            super().accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KeypadForm()
    ex.show()
    sys.exit(app.exec())
