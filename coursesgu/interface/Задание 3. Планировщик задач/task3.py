import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QDate


class EventPlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task3.ui', self)
        self.button_event_add.clicked.connect(self.on_click_event_add)

    def on_click_event_add(self):
        event_name = self.edit_event_name.text()
        event_time = self.edit_event_time.time()
        event_date = self.edit_event_date.selectedDate()
        print(event_name)
        print(event_time)
        print(event_date)
        self.update_after_event_add()

    def update_after_event_add(self):
        self.edit_event_name.clear()
        # self.edit_event_time.clear()
        # self.calendarEvent.setSelectedDate(QDate(2024, 3, 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = EventPlanner()
    widget.show()
    sys.exit(app.exec())
