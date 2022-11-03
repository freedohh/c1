import sys
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
import hh_1
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = hh_1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText('E:/Desktop/c')
        self.ui.lineEdit_2.setText('ceshi')
        self.ui.pushButton2.clicked.connect(self.found_dir)
        self.ui.pushButton2.clicked.connect(self.ceshi)

        self.ui.radioButton27.setChecked(True)
        self.ui.radioButton29.setChecked(True)
        self.ui.radioButton31.setChecked(True)
        self.ui.radioButton33.setChecked(True)
        self.ui.radioButton35.setChecked(True)
        self.ui.radioButton37.setChecked(True)
        self.ui.radioButton39.setChecked(True)
        self.ui.radioButton41.setChecked(True)
        self.ui.graphicsView1.setBackground('w')
        self.ui.graphicsView2.setBackground('w')
        self.ui.graphicsView3.setBackground('w')
        self.ui.graphicsView4.setBackground('w')
        self.ui.graphicsView5.setBackground('w')
        self.ui.graphicsView6.setBackground('w')
        self.ui.graphicsView7.setBackground('w')
        self.ui.graphicsView8.setBackground('w')
        self.ui.graphicsView9.setBackground('w')
        self.ui.graphicsView10.setBackground('w')
        self.ui.graphicsView11.setBackground('w')
        self.ui.graphicsView12.setBackground('w')
    def ceshi(self):
        from win32com import client
        oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
        oDesktop = oAnsoftApp.getAppDesktop()
        oDesktop.RestoreWindow()
        oProject = oDesktop.SetActiveProject("ceshi")
        oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
        oModule = oDesign.GetModule("ReportSetup")

        oModule.ExportToFile("Torque", r'{}/{}'.format(self.a, 'Torque.csv'), False)
        pg = self.image('Torque.csv')
        self.ui.graphicsView1.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')
        # 设置坐标坐标轴标签
        self.ui.graphicsView1.setLabel('left', 'LOSS')
        # 设置底部坐标轴标签
        self.ui.graphicsView1.setLabel('bottom', 'epoch')
        self.ui.graphicsView1.showGrid(x=True, y=True, alpha=0.1)

        oModule.ExportToFile('Currents', r'{}/{}'.format(self.a, 'Currents.csv'), False)
        pg = self.image('Currents.csv')
        self.ui.graphicsView2.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

        oModule.ExportToFile("Induced Voltages", r'{}/{}'.format(self.a, 'Induced Voltages.csv'),
                             False)
        pg = self.image('Induced Voltages.csv')
        self.ui.graphicsView3.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r', title="大窗口")

        oModule.ExportToFile("Flux Linkages", r'{}/{}'.format(self.a, 'Flux Linkages.csv'), False)
        pg = self.image('Flux Linkages.csv')
        self.ui.graphicsView4.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

    def image(self, name):
        pg = pd.read_csv(r'{}/{}'.format(self.a, name))
        return pg
    def found_dir(self):
        self.a = self.ui.lineEdit.text()+'/'+self.ui.lineEdit_2.text()
        if not os.path.exists(self.a): os.makedirs(self.a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())