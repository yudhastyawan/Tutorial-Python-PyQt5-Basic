#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SpinBox")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("SpinBox")
        layout.addWidget(label, 0, 0)

        spinbox = QSpinBox()
        spinbox.setMinimum(0)
        spinbox.setMaximum(100)
        spinbox.setValue(25)
        spinbox.valueChanged.connect(self.on_spin_box_changed)
        layout.addWidget(spinbox, 0, 1)

    def on_spin_box_changed(self, text):
        print("SpinBox value: %i" % (text))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
