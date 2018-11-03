#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        commandlinkbutton1 = QCommandLinkButton()
        commandlinkbutton1.setDescription("CommandLinkButton 1")
        commandlinkbutton1.clicked.connect(self.on_button_clicked)
        layout.addWidget(commandlinkbutton1, 0, 0)

        commandlinkbutton2 = QCommandLinkButton()
        commandlinkbutton2.setDescription("CommandLinkButton 2")
        commandlinkbutton2.clicked.connect(self.on_button_clicked)
        layout.addWidget(commandlinkbutton2, 1, 0)

    def on_button_clicked(self):
        commandlinkbutton = self.sender()

        print("%s clicked!" % (commandlinkbutton.description()))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
