import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QPointF, QRectF

class DrawLabel(QLabel):
    def paintEvent(self, a0):
        if self.draw:
            self.drawCircle()
        self.draw = True
    draw = False
    def drawCircle(self):
        qp = QPainter(self)
        R = randint(20, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.width()//2 - R//2, self.height()//2 - R//2, R, R)

class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.label = DrawLabel("", self)
        self.label.setGeometry(50, 50, 530, 550)
        self.label.setStyleSheet("background-color: pink")
        self.pushButton.clicked.connect(self.label.update)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())