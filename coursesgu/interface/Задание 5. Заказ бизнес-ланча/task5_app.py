import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QButtonGroup, QVBoxLayout, QRadioButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from task5_ui import Ui_Form


class OrderBusinessLunch(QWidget, Ui_Form):
    file_in_name: str = 'menu.json'
    file_out_name: str = 'order.json'
    menu: dict[str, list[str]]
    radio_button_index: int = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_info.hide()
        self.get_menu()
        self.group_soups = QButtonGroup()
        self.update_group(
            position='soups', widget=self.widget_soups, group=self.group_soups, layout=self.layout_soups
        )
        self.group_main = QButtonGroup()
        self.update_group(
            position='main', widget=self.widget_main, group=self.group_main, layout=self.layout_main
        )
        self.group_salads = QButtonGroup()
        self.update_group(
            position='salads', widget=self.widget_salads, group=self.group_salads, layout=self.layout_salads
        )
        self.group_desserts = QButtonGroup()
        self.update_group(
            position='desserts', widget=self.widget_desserts, group=self.group_desserts, layout=self.layout_desserts
        )
        self.group_drinks = QButtonGroup()
        self.update_group(
            position='drinks', widget=self.widget_drinks, group=self.group_drinks, layout=self.layout_drinks
        )
        self.button_order.clicked.connect(self.on_click_order)

    def on_check_state_changed(self, state: Qt.CheckState):
        group = QButtonGroup()
        if self.sender() is self.check_box_soups:
            group = self.group_soups
        elif self.sender() is self.check_box_main:
            group = self.group_main
        elif self.sender() is self.check_box_salads:
            group = self.group_salads
        elif self.sender() is self.check_box_desserts:
            group = self.group_desserts
        elif self.sender() is self.check_box_drinks:
            group = self.group_drinks
        if state is Qt.CheckState.Checked:
            group.setExclusive(True)
            for button in group.buttons():
                button.setEnabled(True)
        else:
            group.setExclusive(False)
            for button in group.buttons():
                button.setAutoExclusive(False)
                button.setChecked(False)
                button.repaint()
                button.setAutoExclusive(True)
                button.setEnabled(False)

    def update_group(self, position: str, widget: QWidget, group: QButtonGroup, layout: QVBoxLayout):
        for dish in self.menu[position]:
            radio_button = QRadioButton(text=dish, parent=widget)
            font = QFont()
            font.setPointSize(16)
            radio_button.setFont(font)
            radio_button.setObjectName(f'radio_button_{self.radio_button_index}')
            group.addButton(radio_button)
            layout.addWidget(radio_button)
            self.radio_button_index += 1

    def on_click_order(self):
        checked_soup: str = ''
        checked_main: str = ''
        checked_salad: str = ''
        checked_dessert: str = ''
        checked_drink: str = ''
        positions_checked: int = 0
        if self.check_box_soups.isChecked() and self.group_soups.checkedId() != -1:
            checked_soup: str = self.group_soups.checkedButton().text()
            positions_checked += 1
        if self.check_box_main.isChecked() and self.group_main.checkedId() != -1:
            checked_main: str = self.group_main.checkedButton().text()
            positions_checked += 1
        if self.check_box_salads.isChecked() and self.group_salads.checkedId() != -1:
            checked_salad: str = self.group_salads.checkedButton().text()
            positions_checked += 1
        if self.check_box_desserts.isChecked() and self.group_desserts.checkedId() != -1:
            checked_dessert: str = self.group_desserts.checkedButton().text()
            positions_checked += 1
        if self.check_box_drinks.isChecked() and self.group_drinks.checkedId() != -1:
            checked_drink: str = self.group_drinks.checkedButton().text()
            positions_checked += 1
        if positions_checked < 2:
            self.label_info.show()
        else:
            self.set_order(
                soup=checked_soup if checked_soup is not None else '',
                main=checked_main if checked_main is not None else '',
                salad=checked_salad if checked_salad is not None else '',
                dessert=checked_dessert if checked_dessert is not None else '',
                drink=checked_drink if checked_drink is not None else ''
            )
            self.label_info.hide()
            self.button_order.setText('Ваш заказ принят')
            self.button_order.setEnabled(False)

    def get_menu(self):
        with open(self.file_in_name, 'r', encoding='utf-8') as file_in:
            self.menu: dict[str, list[str]] = json.load(file_in)

    def set_order(self, soup: str, main: str, salad: str, dessert: str, drink: str):
        with open(self.file_out_name, 'w', encoding='utf-8') as file_out:
            json.dump(
                obj={'soup': soup, 'main': main, 'salad': salad, 'dessert': dessert, 'drink': drink},
                fp=file_out,
                ensure_ascii=False,
                indent=2
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OrderBusinessLunch()
    ex.show()
    sys.exit(app.exec())
