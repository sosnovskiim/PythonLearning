import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QDate, QTime


class EventPlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task3.ui', self)
        self.button_event_add.clicked.connect(self.on_click_event_add)

    def on_click_event_add(self):
        event_name: str = self.edit_event_name.text()
        event_time: QTime = self.edit_event_time.time()
        event_date: QDate = self.edit_event_date.selectedDate()
        self.list_of_events.addItem(
            f'{event_name}, '
            f'{event_time.hour():0>2}:{event_time.minute():0>2}, '
            f'{event_date.day():0>2}.{event_date.month():0>2}.{event_date.year():0>2}'
        )
        self.update_after_event_add()

    def update_after_event_add(self):
        self.edit_event_name.clear()
        self.edit_event_time.setTime(QTime(0, 0, 0, 0))
        # self.calendarEvent.setSelectedDate(QDate.currentDate())
        # Сортировка событий по времени наступления от самого раннего к самому позднему


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = EventPlanner()
    widget.show()
    sys.exit(app.exec())
