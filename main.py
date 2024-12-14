import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6.QtGui import QColor, QPainter, QPixmap, QImage
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.image = None
        self.pushButton = None
        self.pixmap = None
        self.init2()

    def init2(self):
        self.pushButton = QPushButton('Click', self)
        self.pushButton.move(2, 525)
        self.pushButton.resize(520, 23)
        self.pixmap = QLabel(self)
        self.pixmap.move(0, 0)
        self.pixmap.resize(520, 520)
        self.image = QImage(520, 520, QImage.Format.Format_RGB32)
        self.image.fill(QColor(255, 255, 255))
        pixmap = QPixmap(self.image)
        self.pixmap.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        qp = QPainter()
        qp.begin(self.image)
        qp.setBrush(QColor('yellow'))
        x1, y1 = randint(0, 510), randint(0, 510)
        if max(x1, y1) == x1:
            x2 = y2 = randint(10, 520 - x1)
        else:
            x2 = y2 = randint(10, 520 - y1)
        qp.drawEllipse(x1, y1, x2, y2)
        qp.end()
        pixmap = QPixmap(self.image)
        self.pixmap.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle = Circle()
    circle.show()
    sys.exit(app.exec())
