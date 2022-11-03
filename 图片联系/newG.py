import sys
import pandas as pd
import os, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
import random
import untitled
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = untitled.Ui_MainWindow()
        self.ui.setupUi(self)
        cc = pd.read_csv('Torque.csv')
        self.ui.graphicsView.setBackground('w')
        self.ui.graphicsView.plot(cc.iloc[:,0],cc.iloc[:,1],pen='r')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())

