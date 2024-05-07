import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from task4_ui import Ui_Form


class ImageViewer(QWidget, Ui_Form):
    images: list[str]
    current_image: int = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_go_to_first.clicked.connect(self.on_click_go_to_first)
        self.button_go_to_previous.clicked.connect(self.on_click_go_to_previous)
        self.button_go_to_next.clicked.connect(self.on_click_go_to_next)
        self.button_go_to_last.clicked.connect(self.on_click_go_to_last)
        os.chdir(os.path.join(os.curdir, 'images'))
        self.images = [image for image in os.listdir()]
        self.update_image(index=self.current_image)

    def on_click_go_to_first(self):
        self.current_image = 0
        self.update_image(index=self.current_image)

    def on_click_go_to_previous(self):
        self.current_image -= 1
        self.update_image(index=self.current_image)

    def on_click_go_to_next(self):
        self.current_image += 1
        self.update_image(index=self.current_image)

    def on_click_go_to_last(self):
        self.current_image = len(self.images) - 1
        self.update_image(index=self.current_image)

    def update_image(self, index: int):
        if index == 0:
            self.button_go_to_first.setEnabled(False)
            self.button_go_to_previous.setEnabled(False)
        else:
            self.button_go_to_first.setEnabled(True)
            self.button_go_to_previous.setEnabled(True)
        if index == len(self.images) - 1:
            self.button_go_to_last.setEnabled(False)
            self.button_go_to_next.setEnabled(False)
        else:
            self.button_go_to_last.setEnabled(True)
            self.button_go_to_next.setEnabled(True)
        self.label_image.setPixmap(
            QPixmap(self.images[index]).scaled(
                self.label_image.width(),
                self.label_image.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageViewer()
    ex.show()
    sys.exit(app.exec())
