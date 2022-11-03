#!-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
import hh_11

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = hh_11.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushbutton)
        self.ui.checkBox.stateChanged.connect(self.changecheckBok)
    def pushbutton(self):
        if self.ui.pushButton.isChecked():
            print(1)
        else:
            print(2)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())