import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
progbar = QProgressBar()
progbar.show()

for i in range(100):
    progbar.setValue(i)
    app.processEvents()
    time.sleep(0.1)
progbar.close()
sys.exit(app.exec_())