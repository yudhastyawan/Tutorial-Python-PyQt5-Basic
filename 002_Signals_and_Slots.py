import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Signals and Slots")

        # --------------make two buttons-------------
        button1 = QPushButton()
        button1.setText("Button 1")
        # action clicked
        button1.clicked.connect(self.b1_clicked)

        button2 = QPushButton()
        button2.setText("Button 2")
        # action clicked
        button2.clicked.connect(self.b2_clicked)

        # --------------input to layout--------------
        widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(button1)
        main_layout.addWidget(button2)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def b1_clicked(self):
        print("button1 clicked")

    def b2_clicked(self):
        print("button2 clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
