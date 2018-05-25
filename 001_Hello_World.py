import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Hello World")
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.label.setText("Hello World")
        self.label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())