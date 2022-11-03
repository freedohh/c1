import hh
import sys
import pandas as pd
import os, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = hh.Ui_MainWindow()
        self.ui.setupUi(self)
        self.xx = 300
        self.yy = 400
        self.ui.pushButton.clicked.connect(self.get_wav_file)
        self.ui.pushButton_2.clicked.connect(self.max)
    def get_wav_file(self):  # 设置文件路径按钮
        self.file_path= r'E:/Desktop/c/Currents.png'
        print(self.file_path)
        self.image8()
    def max(self):
        self.xx /= 0.9
        self.yy /= 0.9
        self.image8()
    def image8(self):

        pix = QPixmap('{}'.format(self.file_path))
        self.ui.label.setGeometry(0,250,self.xx,self.yy)
        self.ui.label.setPixmap(pix)

        self.ui.label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())