import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('view')
        self.widget = QPushButton()
        self.widget.setText('Click')
        self.widget.clicked.connect(self.processing)
        self.setCentralWidget(self.widget)
        self.stat = self.statusBar()
        self.lb = QLabel()
        self.lb.setText('aku')
        self.stat.addWidget(self.lb)
        # time.sleep(100)


    def processing(self):
        self.lb.setText('yes')
        # self.process = QDialog()
        # self.process.setModal(True)
        # self.process.show()
        # # self.process.setWindowFlag(Qt.WindowStaysOnTopHint)
        # # self.setMosetHidden(True)
        # time.sleep(2)
        # self.process.close()
        # # self.setDisabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    # qApp.exec_()
    sys.exit(app.exec_())