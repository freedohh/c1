import sys
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
import untitled,hh3,untitled1
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = untitled.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pop)
    def pop(self):
        import untitled1
        self.one = untitled1.Ui_MainWindow()
        self.one.show()
        self.one.pushButton.clicked.connect(self.com)
    def com(self):
        hh3.found(self.ui.lineEdit.text(),self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())