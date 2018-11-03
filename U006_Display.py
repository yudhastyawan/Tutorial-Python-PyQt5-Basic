import sys
import numpy as np
import matplotlib as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar

def data():
    nx = 30
    ny = 20
    nz = 50

    vx = np.linspace(1500, 3000, nx)
    vy = np.linspace(1500, 4000, ny)
    vz = np.linspace(1500, 8000, nz)

    vxy = np.sqrt(np.transpose(np.mat(vy)) * np.mat(vx))
    vxyz = []
    for i in range(len(vz)):
        vxyz.append(np.sqrt(vxy * vz[i]))
    vxyz = np.array(vxyz).transpose()

    x = np.linspace(0, 50, nx)
    y = np.linspace(0, 40, ny)
    Z = np.linspace(0, 100, nz)

    Y, X = np.meshgrid(y, x)

    return X,Y,Z,vxyz

class QT5MplCanvas(FigureCanvas):
    def __init__(self,X,Y,Z,data,n,parent):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(121)
        g = data
        data = data[:,:,int(np.fix(n*(len(Z)-1)/np.max(Z)))]
        self.axes.imshow(data, cmap=plt.cm.jet, interpolation='nearest', origin='lower', extent=[np.min(X), np.max(X), np.min(Y), np.max(Y)],
                         vmin=np.min(g), vmax=np.max(g))

        self.axes2 = self.fig.add_subplot(122, projection='3d')

        FigureCanvas.__init__(self, self.fig)
        Axes3D.mouse_init(self.axes2)
        cset = self.axes2.contourf(X, Y, data, min(data.shape), zdir='z', offset=n, cmap=plt.cm.jet, vmin = np.min(g), vmax = np.max(g))

        self.axes2.set_zlim((np.max(Z), np.min(Z)))
        self.fig.colorbar(cset)

        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class ApplicationWindow(QMainWindow):
    def __init__(self):
        global data
        QMainWindow.__init__(self)
        self.setWindowTitle("Mpl vs PyQt5")
        self.sl = QSlider(Qt.Horizontal)
        self.lb = QLabel()
        self.X, self.Y, self.Z, self.data = data()
        self.sl.setMinimum(min(self.Z))
        self.sl.setMaximum(max(self.Z))
        self.sl.setValue(min(self.Z))
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(self.Z[5]-self.Z[0])
        self.sl.valueChanged.connect(self.valuechange)
        self.lb.setText(str(self.sl.value()))
        layout2 = QHBoxLayout()
        layout2.addWidget(self.lb)
        layout2.addWidget(self.sl)

        self.main_widget = QWidget(self)
        self.vbl = QVBoxLayout(self.main_widget)

        vbl = self.vbl
        # print(data.shape)
        self.qmc = QT5MplCanvas(self.X,self.Y,self.Z,self.data,self.sl.value(),self.main_widget)
        self.ntb = NavigationToolbar(self.qmc,self.main_widget)

        vbl.addLayout(layout2)
        vbl.addWidget(self.qmc)
        vbl.addWidget(self.ntb)

        self.main_widget.setFocus()

        self.setCentralWidget(self.main_widget)

    def valuechange(self):
        size = self.sl.value()
        self.lb.setText(str(size))
        self.vbl.removeWidget(self.qmc)
        self.vbl.removeWidget(self.ntb)
        self.qmc = QT5MplCanvas(self.X, self.Y, self.Z, self.data, size, self.main_widget)
        self.ntb = NavigationToolbar(self.qmc, self.main_widget)
        self.vbl.addWidget(self.qmc)
        self.vbl.addWidget(self.ntb)
        self.main_widget.setFocus()

App = QApplication(sys.argv)
mpl = ApplicationWindow()
mpl.show()
sys.exit(App.exec_())
