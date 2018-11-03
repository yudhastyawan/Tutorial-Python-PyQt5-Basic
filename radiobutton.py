#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Brazil")
        radiobutton.setChecked(True)
        radiobutton.country = "Brazil"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Argentina")
        radiobutton.country = "Argentina"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Ecuador")
        radiobutton.country = "Ecuador"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 2)

    def on_radio_button_toggled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            print("Selected country is %s" % (radiobutton.country))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
