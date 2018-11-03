import sys

from PyQt5.QtWidgets import *

class QCustomTabWidget (QTabWidget):
    def __init__ (self, parent = None):
        super(QCustomTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)
        for i in range(1, 10):
            self.addTab(QWidget(), 'Tab %d' % i)

    def closeTab (self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

myQApplication = QApplication([])
myQCustomTabWidget = QCustomTabWidget()
myQCustomTabWidget.show()
sys.exit(myQApplication.exec_())