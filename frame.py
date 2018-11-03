#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        frame = QFrame()
        frame.setWindowTitle("Frame")
        frame.setFrameShape(QFrame.Box)
        frame.setFixedSize(150, 150)
        layout.addWidget(frame)

        box = QHBoxLayout()
        frame.setLayout(box)

        label = QLabel("Label in a Frame")
        box.addWidget(label)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
