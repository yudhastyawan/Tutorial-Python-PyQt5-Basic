from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

class Main(QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        # self.setWindowFlag(Qt.FramelessWindowHint,True)

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('tux.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    App.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    main = Main()
    main.show()
    splash.finish(main)
    sys.exit(App.exec_())