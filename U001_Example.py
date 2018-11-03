import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.Dense1Pattern)
        self.mdi.setBackground(brush)
        self.mdi.setViewMode(QMdiArea.TabbedView)
        self.mdi.setTabShape(QTabWidget.Triangular)
        self.mdi.setTabPosition(QTabWidget.West)
        self.sub = SubWindow()
        self.mdi.addSubWindow(self.sub)
        for i in range(1):
            self.sub2 = QWidget()
            self.mdi.addSubWindow(self.sub2)
        self.mdi.show()

class SubWindow(QMainWindow):
    def __init__(self,parent = None):
        super(SubWindow, self).__init__(parent)
        self.setWindowTitle("Aku")
        # self.mb = self.menuBar()
        # self.mb.addMenu("File")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())