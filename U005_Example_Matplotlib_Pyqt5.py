import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar

class QT5MplCanvas(FigureCanvas):
    def __init__(self,parent):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.x = np.arange(0.0,3.0,0.01)
        self.y = np.cos(2*np.pi*self.x)
        self.axes.plot(self.x, self.y)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Mpl vs PyQt5")

        self.main_widget = QWidget(self)
        vbl = QVBoxLayout(self.main_widget)
        qmc = QT5MplCanvas(self.main_widget)
        ntb = NavigationToolbar(qmc,self.main_widget)

        vbl.addWidget(qmc)
        vbl.addWidget(ntb)

        self.main_widget.setFocus()

        self.setCentralWidget(self.main_widget)

App = QApplication(sys.argv)
mpl = ApplicationWindow()
mpl.show()
sys.exit(App.exec_())

