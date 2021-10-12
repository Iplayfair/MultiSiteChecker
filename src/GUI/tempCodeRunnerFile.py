import sys
import MultiSiteChecker as Msc
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100,100,1000,750)
    win.setWindowTitle("MultiSiteChecker")
    win.show()
    
    sys.exit(app.exec_())

window()