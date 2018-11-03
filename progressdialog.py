#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time

class Window(QProgressDialog):
    def __init__(self):
        QProgressDialog.__init__(self)
        self.setWindowTitle("ProgressDialog")
        self.setLabelText("ProgressDialog to indicate the status of a process...")
        self.canceled.connect(self.close)
        self.setRange(0, 100)

        for count in range(self.minimum(), self.maximum() + 1):
            self.setValue(count)
            qApp.processEvents()
            time.sleep(0.05)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
