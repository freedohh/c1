import sys
import time

import pandas as pd
import os,time
from PyQt5.QtCore import QTimer,QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene,QAction,QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage
import h1
import hh10
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = h1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.poph2)
        self.ui.pushButton.clicked.connect(self.que)
    def poph2(self):
        import h2
        self.one = h2.Ui_MainWindow()
        self.one.show()
        self.one.pushButton.clicked.connect(self.re)

    def re(self):
        ree = hh10.register(self.one.lineEdit.text(),self.one.lineEdit_2.text())
        if ree == 1:
            self.poph4('注册成功，即将进入登录界面')
            self.one.close()
    def poph4(self,a):
        import h4
        self.four = h4.AutoCloseWindow()
        self.four.label.setText(a)
        self.four.show()
        QTimer.singleShot(1000,self.four.close)

    def que(self):
        qu = hh10.query1(self.ui.lineEdit.text(),self.ui.lineEdit_2.text())
        if qu == 1:
            self.poph4('登录成功，即将进入系统')
            self.close()
            self.poph3()
        else:
            self.poph4('密码错误，请重新输入')

    def poph3(self):
        import h3
        self.three = h3.Ui_MainWindow()
        self.di()
        self.three.show()
        self.three.pushButton.clicked.connect(self.es)
        self.three.pushButton_2.clicked.connect(self.dele)
    def es(self):
        ee = hh10.query2(self.three.lineEdit.text())
        if ee == 1:
            self.poph4('名字重复，请检查名字')
        else:
            hh10.establish(self.three.lineEdit.text(),self.three.lineEdit_2.text(),self.three.lineEdit_3.text())
            self.di()
    def dele(self):
        ee = hh10.query2(self.three.lineEdit_4.text())
        if ee == 1:
            self.poph4('已删除{}所有数据'.format(self.three.lineEdit_4.text()))
            hh10.delete(self.three.lineEdit_4.text())
            self.di()
        else:
            self.poph4('未找到该数据')
    def di(self):
        ee = hh10.display()
        x = len(ee)
        y = 3
        self.three.tableWidget.setRowCount(x)
        self.three.tableWidget.setColumnCount(y)
        self.three.tableWidget.setHorizontalHeaderLabels(['name','age','core'])

        for i in range(x):
            for j in range(y):
                data = QTableWidgetItem(str(ee[i][j]))
                self.three.tableWidget.setItem(i,j,data)
        self.three.tableWidget.resizeColumnToContents(x)
        self.three.tableWidget.resizeRowToContents(y)
        self.three.tableWidget.setAlternatingRowColors(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())