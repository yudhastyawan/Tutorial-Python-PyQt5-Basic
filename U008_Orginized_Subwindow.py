from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Main(QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setWindowTitle("Orginized Subwindow")
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        # self.setWindowFlag(Qt.WindowTitleHint,False)

        #set menubar
        self.mbar = self.menuBar()
        self.Sub = self.mbar.addAction("Sub")
        self.Sub.triggered.connect(self.subshow)
        self.Sub2 = self.mbar.addAction("Sub2")
        self.Sub2.triggered.connect(self.subshow2)

        #create mdi
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #add subwindow
        self.subwindow = Subwindow()
        self.mdi.addSubWindow(self.subwindow)
        # self.subwindow.setVisible(False)
        self.subwindow.setHidden(True)
        # self.subwindow.hide()

        # self.subwindow2 = Subwindow2()
        # self.mdi.addSubWindow(self.subwindow2)
        # # self.subwindow.setVisible(False)
        # self.subwindow2.setHidden(True)
        # self.subwindow.hide()

        self.subwindow3 = Subwindow3()
        self.mdi.addSubWindow(self.subwindow3)
        # self.subwindow.setVisible(False)
        # self.subwindow3.setHidden(True)
        self.subwindow3.showMaximized()

    def subshow(self):
        # if(self.subwindow.isVisible() == False):
        self.subwindow.showMaximized()
        # else:
        #     self.subwindow.hide()

    def subshow2(self):
        # if(self.subwindow2.isVisible() == False):
        self.sub2 = Subwindow2()
        self.sub2.show()
        # sub.show()


        # else:
        #     self.subwindow2.hide()

class Subwindow(QMainWindow):
    def __init__(self, parent = None):
        super(Subwindow, self).__init__(parent)
        self.setWindowTitle("Subwindow")
        self.setWindowFlag(Qt.FramelessWindowHint, True)

class Subwindow2(QMainWindow):
    def __init__(self, parent = None):
        super(Subwindow2, self).__init__(parent)

        self.setWindowTitle("Subwindow2")

class Subwindow3(QMainWindow):
    def __init__(self, parent = None):
        super(Subwindow3, self).__init__(parent)
        self.setWindowTitle("Subwindow3")
        self.setWindowFlag(Qt.FramelessWindowHint, True)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(App.exec_())