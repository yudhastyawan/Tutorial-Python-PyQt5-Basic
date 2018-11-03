import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class sliderdemo(QWidget):
    def __init__(self,parent = None):
        super(sliderdemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.l1 = QLabel("Hello")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        layout2 = QVBoxLayout()
        self.l2 = QLabel()
        self.sl = QSlider(Qt.Vertical)
        self.sl.setMinimum(10)
        self.sl.setMaximum(30)
        self.sl.setValue(20)
        self.sl.setTickPosition(QSlider.TicksRight)
        self.sl.setTickInterval(5)
        self.l2.setText(str(self.sl.value()))
        layout2.addWidget(self.l2)
        layout2.addWidget(self.sl)
        layout.addLayout(layout2)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("Slider Demo")

    def valuechange(self):
        size = self.sl.value()
        self.l2.setText(str(size))
        self.l1.setFont(QFont("Arial",size))

def main():
    app = QApplication(sys.argv)
    ex = sliderdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
