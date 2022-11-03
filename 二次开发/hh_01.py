#!-*- coding:utf-8 -*-
import sys
import pandas as pd
import os, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
import hh_1


class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = hh_1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.parementer = ['' for i in range(100)]
        self.ui.pushButton6.clicked.connect(self.change)
        self.ui.pushButton5.clicked.connect(self.change0)
        self.ui.comboBox.currentIndexChanged.connect(self.import_pa)
        self.ui.pushButton4.clicked.connect(self.get_wav_path)
        self.ui.radioButton28.setChecked(True)
        # self.ui.lineEdit.setText('E:/Desktop/c')
        # self.ui.lineEdit_2.setText('CeShi')
        self.ui.pushButton1.clicked.connect(self.found_dir)
        # self.ui.pushButton2.clicked.connect(self.openshow1)
        # self.scene = QGraphicsScene()  # 创建画布
        # self.scene1 = QGraphicsScene()
        # self.ui.graphicsView.setScene(self.scene)  # 把画布添加到窗口
        # self.ui.graphicsView_2.setScene(self.scene1)

        # 需要调整到gui界面中去
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

    def change(self):

        self.ui.stackedWidget.setCurrentIndex(1)

    def change0(self):

        self.ui.stackedWidget.setCurrentIndex(0)

    def found_dir(self):
        self.a = self.ui.lineEdit.text() + '/' + self.ui.lineEdit_2.text()
        if not os.path.exists(self.a): os.makedirs(self.a)
        self.found()

    def import_pa(self):
        try:
            self.mm = pd.read_excel("Electric machinery.xlsx")
            if self.ui.comboBox.currentIndex() == 1:
                self.n = self.mm['12槽']
            if self.ui.comboBox.currentIndex() == 2:
                self.n = self.mm['14槽']
            self.ui.lineEdit1.setText(self.n[0])
            self.ui.lineEdit2.setText(self.n[1])
            self.ui.lineEdit3.setText(self.n[2])
            self.ui.lineEdit4.setText(self.n[3])
            self.ui.lineEdit5.setText(self.n[4])
            self.ui.lineEdit6.setText(self.n[5])
            self.ui.lineEdit7.setText(self.n[6])
            self.ui.lineEdit8.setText(self.n[7])
            self.ui.lineEdit9.setText(self.n[8])
            self.ui.lineEdit10.setText(self.n[9])
            self.ui.lineEdit11.setText(self.n[10])
            self.ui.lineEdit12.setText(self.n[11])
            self.ui.lineEdit13.setText(self.n[12])
            self.ui.lineEdit14.setText(self.n[13])
            self.ui.lineEdit15.setText(self.n[14])
            self.ui.lineEdit16.setText(self.n[15])
            self.ui.lineEdit17.setText(self.n[17])
            self.ui.lineEdit18.setText(self.n[18])
            self.ui.lineEdit19.setText(self.n[19])
            self.ui.lineEdit20.setText(self.n[20])
            self.ui.lineEdit21.setText(self.n[21])
            self.ui.lineEdit22.setText(self.n[22])
            self.ui.lineEdit23.setText(self.n[23])
            self.ui.lineEdit24.setText(self.n[24])
            self.ui.lineEdit25.setText(self.n[25])
            self.ui.lineEdit26.setText(self.n[26])
            self.ui.lineEdit27.setText(self.n[27])
            self.ui.lineEdit28.setText(self.n[31])
            self.ui.lineEdit29.setText(self.n[32])
            self.ui.lineEdit30.setText(self.n[33])
            self.ui.lineEdit31.setText(self.n[34])
            self.ui.lineEdit32.setText(self.n[35])
            self.ui.lineEdit33.setText(self.n[37])
            self.ui.lineEdi34.setText(self.n[38])
            self.ui.lineEdit35.setText(self.n[39])
            self.ui.lineEdit36.setText(self.n[40])
            self.ui.lineEdit37.setText(self.n[41])
            self.ui.lineEdit38.setText(self.n[42])
            self.ui.lineEdit39.setText(self.n[43])
            self.ui.lineEdit40.setText(self.n[44])
            self.ui.lineEdit41.setText(self.n[46])
            self.ui.lineEdit42.setText(self.n[47])
            self.ui.lineEdit43.setText(self.n[48])
            self.ui.lineEdit44.setText(self.n[49])
            self.ui.lineEdit45.setText(self.n[50])
            self.ui.lineEdit46.setText(self.n[51])
            self.ui.lineEdit47.setText(self.n[52])
            self.ui.lineEdit48.setText(self.n[53])
            self.ui.lineEdit49.setText(self.n[54])
            self.ui.lineEdit50.setText(self.n[55])
            self.ui.lineEdit51.setText(self.n[58])
            self.ui.lineEdit52.setText(self.n[59])
            self.ui.lineEdit53.setText(self.n[60])
            self.ui.lineEdit54.setText(self.n[61])
            self.ui.lineEdit55.setText(self.n[62])
            self.ui.lineEdit56.setText(self.n[63])
            self.ui.lineEdit57.setText(self.n[64])
            self.ui.lineEdit58.setText(self.n[65])
            self.ui.lineEdit59.setText(self.n[66])
            self.ui.lineEdit60.setText(self.n[67])
            self.ui.lineEdit61.setText(self.n[68])
            if self.n[16] == '1':
                self.ui.radioButton1.setChecked(True)
            elif self.n[16] == '2':
                self.ui.radioButton2.setChecked(True)
            elif self.n[16] == '3':
                self.ui.radioButton3.setChecked(True)
            else:
                self.ui.radioButton4.setChecked(True)
            if self.n[28] == 'Lap':
                self.ui.radioButton5.setChecked(True)
            else:
                self.ui.radioButton6.setChecked(True)
            if self.n[29] == '1':
                self.ui.radioButton7.setChecked(True)
            elif self.n[29] == '2':
                self.ui.radioButton8.setChecked(True)
            else:
                self.ui.radioButton9.setChecked(True)
            if self.n[30] == '1':
                self.ui.radioButton10.setChecked(True)
            elif self.n[30] == '2':
                self.ui.radioButton11.setChecked(True)
            elif self.n[30] == '3':
                self.ui.radioButton12.setChecked(True)
            else:
                self.ui.radioButton13.setChecked(True)
            if self.n[36] == 'True':
                self.ui.radioButton14.setChecked(True)
            else:
                self.ui.radioButton15.setChecked(True)
            if self.n[45] == 'Cylinder':
                self.ui.radioButton16.setChecked(True)
            else:
                self.ui.radioButton17.setChecked(True)
            if self.n[56] == 'True':
                self.ui.radioButton18.setChecked(True)
            else:
                self.ui.radioButton19.setChecked(True)
            if self.n[57] == '1':
                self.ui.radioButton20.setChecked(True)
            elif self.n[57] == '2':
                self.ui.radioButton21.setChecked(True)
            else:
                self.ui.radioButton22.setChecked(True)
        except Exception as e:
            self.ui.textEdit_2.setText("导入参数出错，请检查参数文件是否存在或不正确的修改")

    def exchange_pa(self):
        self.parementer[0] = self.ui.lineEdit1.text()
        self.parementer[1] = self.ui.lineEdit2.text()
        self.parementer[2] = self.ui.lineEdit3.text()
        self.parementer[3] = self.ui.lineEdit4.text()
        self.parementer[4] = self.ui.lineEdit5.text()
        self.parementer[5] = self.ui.lineEdit6.text()
        self.parementer[6] = self.ui.lineEdit7.text()
        self.parementer[7] = self.ui.lineEdit8.text()
        self.parementer[8] = self.ui.lineEdit9.text()
        self.parementer[9] = self.ui.lineEdit10.text()
        self.parementer[10] = self.ui.lineEdit11.text()
        self.parementer[11] = self.ui.lineEdit12.text()
        self.parementer[12] = self.ui.lineEdit13.text()
        self.parementer[13] = self.ui.lineEdit14.text()
        self.parementer[14] = self.ui.lineEdit15.text()
        self.parementer[15] = self.ui.lineEdit16.text()
        self.parementer[17] = self.ui.lineEdit17.text()
        self.parementer[18] = self.ui.lineEdit18.text()
        self.parementer[19] = self.ui.lineEdit19.text()
        self.parementer[20] = self.ui.lineEdit20.text()
        self.parementer[21] = self.ui.lineEdit21.text()
        self.parementer[22] = self.ui.lineEdit22.text()
        self.parementer[23] = self.ui.lineEdit23.text()
        self.parementer[24] = self.ui.lineEdit24.text()
        self.parementer[25] = self.ui.lineEdit25.text()
        self.parementer[26] = self.ui.lineEdit26.text()
        self.parementer[27] = self.ui.lineEdit27.text()
        self.parementer[31] = self.ui.lineEdit28.text()
        self.parementer[32] = self.ui.lineEdit29.text()
        self.parementer[33] = self.ui.lineEdit30.text()
        self.parementer[34] = self.ui.lineEdit31.text()
        self.parementer[35] = self.ui.lineEdit32.text()
        self.parementer[37] = self.ui.lineEdit33.text()
        self.parementer[38] = self.ui.lineEdi34.text()
        self.parementer[39] = self.ui.lineEdit35.text()
        self.parementer[40] = self.ui.lineEdit36.text()
        self.parementer[41] = self.ui.lineEdit37.text()
        self.parementer[42] = self.ui.lineEdit38.text()
        self.parementer[43] = self.ui.lineEdit39.text()
        self.parementer[44] = self.ui.lineEdit40.text()
        self.parementer[46] = self.ui.lineEdit41.text()
        self.parementer[47] = self.ui.lineEdit42.text()
        self.parementer[48] = self.ui.lineEdit43.text()
        self.parementer[49] = self.ui.lineEdit44.text()
        self.parementer[50] = self.ui.lineEdit45.text()
        self.parementer[51] = self.ui.lineEdit46.text()
        self.parementer[52] = self.ui.lineEdit47.text()
        self.parementer[53] = self.ui.lineEdit48.text()
        self.parementer[54] = self.ui.lineEdit49.text()
        self.parementer[55] = self.ui.lineEdit50.text()
        self.parementer[58] = self.ui.lineEdit51.text()
        self.parementer[59] = self.ui.lineEdit52.text()
        self.parementer[60] = self.ui.lineEdit53.text()
        self.parementer[61] = self.ui.lineEdit54.text()
        self.parementer[62] = self.ui.lineEdit55.text()
        self.parementer[63] = self.ui.lineEdit56.text()
        self.parementer[64] = self.ui.lineEdit57.text()
        self.parementer[65] = self.ui.lineEdit58.text()
        self.parementer[66] = self.ui.lineEdit59.text()
        self.parementer[67] = self.ui.lineEdit60.text()
        self.parementer[68] = self.ui.lineEdit61.text()
        if self.ui.radioButton1.isChecked():
            self.parementer[16] = '1'
        elif self.ui.radioButton2.isChecked():
            self.parementer[16] = '2'
        elif self.ui.radioButton3.isChecked():
            self.parementer[16] = '3'
        else:
            self.parementer[16] = '4'
        if self.ui.radioButton5.isChecked():
            self.parementer[28] = 'Lap'
        else:
            self.parementer[28] = 'Wave'
        if self.ui.radioButton7.isChecked():
            self.parementer[29] = '1'
        elif self.ui.radioButton8.isChecked():
            self.parementer[29] = '2'
        else:
            self.parementer[29] = '3'
        if self.ui.radioButton10.isChecked():
            self.parementer[30] = '1'
        elif self.ui.radioButton11.isChecked():
            self.parementer[30] = '2'
        elif self.ui.radioButton12.isChecked():
            self.parementer[30] = '3'
        else:
            self.parementer[30] = '4'
        if self.ui.radioButton14.isChecked():
            self.parementer[36] = 'True'
        else:
            self.parementer[36] = 'False'
        if self.ui.radioButton16.isChecked():
            self.parementer[45] = 'Cylinder'
        else:
            self.parementer[45] = 'Pancake'
        if self.ui.radioButton18.isChecked():
            self.parementer[56] = 'True'
        else:
            self.parementer[56] = 'False'
        if self.ui.radioButton20.isChecked():
            self.parementer[57] = 'ConstSpeed'
        elif self.ui.radioButton21.isChecked():
            self.parementer[57] = 'ConstTorque'
        else:
            self.parementer[57] = 'LinerTorque'

    def get_wav_path(self):
        self.file_path = QFileDialog.getExistingDirectory(None, "请选择文件夹", os.getcwd())
        self.ui.lineEdit.setText(self.file_path)

    def get_wav_file(self):  # 设置文件路径按钮
        self.file_path = QFileDialog.getOpenFileName(None, "请选择文件", os.getcwd())
        self.ui.lineEdit54.setText(self.file_path[0])

    # def resume(self):  # 用来恢复/启动run
    #     with self.state:  # 在该条件下操作
    #         self.paused = False
    #         self.state.notify()  # Unblock self if waiting.
    #
    # def pause(self):  # 用来暂停run
    #     self.thr.wait()
    def found(self):
        try:
            thr = threading.Thread(target=self.caculate)
            # self.state = threading.Condition()
            thr.start()
        except Exception as e:
            self.ui.textEdit_2.setText("计算出错了")
            print(e)

    def caculate(self):
        try:
            self.exchange_pa()
            from win32com import client
            oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
            oDesktop = oAnsoftApp.getAppDesktop()
            oDesktop.RestoreWindow()
            oProject = oDesktop.NewProject()
            oProject.InsertDesign("RMxprt", "RMxprtDesign1", "Permanent-Magnet DC Motor", "")
            oDesign = oProject.SetActiveDesign("RMxprtDesign1")
            oEditor = oDesign.SetActiveEditor("Machine")
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Machine",
                        [
                            "NAME:PropServers",
                            "Machine"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Number of Poles",
                                "Value:=", self.parementer[0]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Machine",
                        [
                            "NAME:PropServers",
                            "Machine"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Frictional Loss",
                                "Value:=", self.parementer[1]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Machine",
                        [
                            "NAME:PropServers",
                            "Machine"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Windage Loss",
                                "Value:=", self.parementer[2]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Machine",
                        [
                            "NAME:PropServers",
                            "Machine"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Reference Speed",
                                "Value:=", self.parementer[3]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Stator",
                        [
                            "NAME:PropServers",
                            "Stator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Outer Diameter",
                                "Value:="	, self.parementer[4]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Stator",
                        [
                            "NAME:PropServers",
                            "Stator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Inner Diameter",
                                "Value:="		, self.parementer[5]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Stator",
                        [
                            "NAME:PropServers",
                            "Stator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Length",
                                "Value:="		, self.parementer[6]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Stator",
                        [
                            "NAME:PropServers",
                            "Stator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Stacking Factor",
                                "Value:="		, self.parementer[7]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Stator",
                        [
                            "NAME:PropServers",
                            "Stator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Steel Type",
                                "Material:="		, self.parementer[8]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Pole",
                        [
                            "NAME:PropServers",
                            "Stator:Pole"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Embrace",
                                "Value:="		, self.parementer[9]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Pole",
                        [
                            "NAME:PropServers",
                            "Stator:Pole"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Offset",
                                "Value:="	, self.parementer[10]
                            ]
                        ]
                    ]
                ])
            oDefinitionManager = oProject.GetDefinitionManager()
            oDefinitionManager.EditMaterial("TDK_FB6B_20cel",
                                            [
                                                "NAME:TDK_FB6B_20cel",
                                                "CoordinateSystemType:=", "Cartesian",
                                                "BulkOrSurfaceType:="	, 1,
                                                [
                                                    "NAME:PhysicsTypes",
                                                    "set:="			, ["Electromagnetic"]
                                                ],
                                                [
                                                    "NAME:permeability",
                                                    "property_type:="	, "nonlinear",
                                                    "BTypeForSingleCurve:="	, "normal",
                                                    "HUnit:="		, "A_per_meter",
                                                    "BUnit:="		, "tesla",
                                                    "IsTemperatureDependent:=", False,
                                                    [
                                                        "NAME:BHCoordinates",
                                                        [
                                                            "NAME:DimUnits",
                                                            "",
                                                            ""
                                                        ],
                                                        [
                                                            "NAME:Point",
                                                            -302394.391874601,
                                                            0
                                                        ],
                                                        [
                                                            "NAME:Point",
                                                            -151197.195937301,
                                                            0.19
                                                        ],
                                                        [
                                                            "NAME:Point",
                                                            0,
                                                            0.38
                                                        ]
                                                    ],
                                                    [
                                                        "NAME:Temperatures"
                                                    ]
                                                ],
                                                [
                                                    "NAME:magnetic_coercivity",
                                                    "property_type:="	, "VectorProperty",
                                                    "Magnitude:="		, "-302394.391874601A_per_meter",
                                                    "DirComp1:="		, "1",
                                                    "DirComp2:="		, "0",
                                                    "DirComp3:="		, "0"
                                                ]
                                            ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Pole",
                        [
                            "NAME:PropServers",
                            "Stator:Pole"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Magnet Type",
                                "Material:="		, self.parementer[11]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Pole",
                        [
                            "NAME:PropServers",
                            "Stator:Pole"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Magnet Length",
                                "Value:="		, self.parementer[12]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Pole",
                        [
                            "NAME:PropServers",
                            "Stator:Pole"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Magnet Thickness",
                                "Value:="		, self.parementer[13]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Stacking Factor",
                                "Value:="	, self.parementer[14]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Number of Slots",
                                "Value:="		, self.parementer[15]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Slot Type",
                                "SlotType:="		, self.parementer[16]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Outer Diameter",
                                "Value:="		, self.parementer[17]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Inner Diameter",
                                "Value:="		, self.parementer[18]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Length",
                                "Value:="		, self.parementer[19]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Steel Type",
                                "Material:="		, self.parementer[20]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Rotor",
                        [
                            "NAME:PropServers",
                            "Rotor"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Skew Width",
                                "Value:="		, self.parementer[21]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Auto Design",
                                "Value:="		, False
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Hs0",
                                "Value:="		, self.parementer[22]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Hs1",
                                "Value:="		, self.parementer[23]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Hs2",
                                "Value:="		, self.parementer[24]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Bs0",
                                "Value:="		, self.parementer[25]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Bs1",
                                "Value:="		, self.parementer[26]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Slot",
                        [
                            "NAME:PropServers",
                            "Rotor:Slot"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Bs2",
                                "Value:="		, self.parementer[27]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Winding Type",
                                "WindingType:="	, self.parementer[28]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Multiplex Number",
                                "Value:="	, self.parementer[29]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Virtual Slots",
                                "Value:="	, self.parementer[30]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Conductors per Slot",
                                "Value:="		, self.parementer[31]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Coil Pitch",
                                "Value:="		, self.parementer[32]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Number of Strands",
                                "Value:="		, self.parementer[33]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Wire Wrap",
                                "Value:="		, self.parementer[34]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Winding",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Wire Size",
                                "WireSizeWireDiameter:=", self.parementer[35],
                                "WireSizeGauge:="	, "0",
                                "WireSizeWireWidth:="	, "0mm",
                                "WireSizeWireThickness:=", "0mm",
                                "WireSizeMixedWireRectType:=", False,
                                [
                                    "NAME:WireSizeMixedDiameter"
                                ],
                                [
                                    "NAME:WireSizeMixedWidth"
                                ],
                                [
                                    "NAME:WireSizeMixedThickness"
                                ],
                                [
                                    "NAME:WireSizeMixedThicknessMixedFillet"
                                ],
                                [
                                    "NAME:WireSizeMixedThicknessMixedNumber"
                                ]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Input Half-turn Length",
                                "Value:="		, self.parementer[36]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Half Turn Length",
                                "Value:="		, self.parementer[37]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Base Inner Radius",
                                "Value:="		, self.parementer[38]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Tip Inner Diameter",
                                "Value:="		, self.parementer[39]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:End Clearance",
                                "Value:="	, self.parementer[40]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Slot Liner",
                                "Value:="		, self.parementer[41]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Wedge Thickness",
                                "Value:="	, self.parementer[42]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Layer Insulation",
                                "Value:="		, self.parementer[43]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:End/Insulation",
                        [
                            "NAME:PropServers",
                            "Rotor:Winding"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Limited Fill Factor",
                                "Value:="		, self.parementer[44]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Commutator",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Commutator Diameter",
                                "Value:="		, self.parementer[46]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Commutator",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Commutator Length",
                                "Value:="		, self.parementer[47]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Commutator",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Commutator Insulation",
                                "Value:="		, self.parementer[48]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Brush",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Brush Width",
                                "Value:="		, self.parementer[49]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Brush",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Brush Length",
                                "Value:="		, self.parementer[50]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Brush",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Brush Pairs",
                                "Value:="		, self.parementer[51]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Brush",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Brush Displacement",
                                "Value:="	, self.parementer[52]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Brush",
                        [
                            "NAME:PropServers",
                            "Commutator"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Brush Drop",
                                "Value:="		, self.parementer[53]
                            ]
                        ]
                    ]
                ])
            oEditor.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:Shaft",
                        [
                            "NAME:PropServers",
                            "Shaft"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:Magnetic Shaft",
                                "Value:="		, self.parementer[56]
                            ]
                        ]
                    ]
                ])
            oDesign.SetDesignSettings(
                [
                    "NAME:Design Settings Data",
                    "Steel Threshold:="	, 100,
                    "Conductor Threshold:="	, 100000,
                    "Excel Template Path:="	, "",
                    "UDDEnabled:="		, True,
                    "UDD:="			, ["Fractions 1"]
                ])
            oModule = oDesign.GetModule("AnalysisSetup")
            oModule.InsertSetup("PMDC",
                                [
                                    "NAME:Setup1",
                                    "Enabled:="		, True,
                                    [
                                        "NAME:MeshLink",
                                        "ImportMesh:="		, False
                                    ],
                                    "RatedOutputPower:="	, self.parementer[58],
                                    "RatedVoltage:="	, self.parementer[59],
                                    "RatedSpeed:="		, self.parementer[60],
                                    "OperatingTemperature:=", "75cel",
                                    "OperationType:="	, "Motor",
                                    "LoadType:="		, self.parementer[57]
                                ])
            oProject.SaveAs(r"{}/{}.aedt".format(self.a, self.ui.lineEdit_2.text()), True)
            oDesign = oProject.SetActiveDesign("RMxprtDesign1")
            oDesign.Analyze("Setup1")
            oModule = oDesign.GetModule("AnalysisSetup")
            oModule.CreateMaxwellDesign(0, "Setup1", "")
            oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
            oEditor = oDesign.SetActiveEditor("3D Modeler")
            if self.parementer[15] == '12':
                oEditor.Chamfer(
                    [
                        "NAME:Selections",
                        "Selections:="	, "Mag_0,Mag_3,Mag_2,Mag_1",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:ChamferParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [47 ,46],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:=", [],
                            "Vertices:=", [80, 81],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:=", [],
                            "Vertices:=", [69, 70],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:=", [],
                            "Vertices:=", [58, 59],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:=", "Mag_0,Mag_3,Mag_2,Mag_1",
                        "NewPartsModelFlag:=", "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:=", [],
                            "Vertices:="	, [45 ,44],
                            "Radius:=", self.parementer[66],
                            "Setback:=", "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:=", [],
                            "Vertices:="	, [79 ,78],
                            "Radius:=", self.parementer[66],
                            "Setback:=", "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:=", [],
                            "Vertices:="	, [68 ,67],
                            "Radius:=", self.parementer[66],
                            "Setback:=", "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:=", [],
                            "Vertices:="	, [57 ,56],
                            "Radius:=", self.parementer[66],
                            "Setback:=", "0mm"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:=", "Rotor",
                        "NewPartsModelFlag:=", "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:=", [],
                            "Vertices:="	, [339 ,338, 571, 572, 570, 569, 550, 551, 548, 529, 549, 530, 528, 527, 508, 509, 507, 506
                                , 488, 487, 486, 485, 466, 467, 464, 465, 445, 446, 444, 443, 425, 424, 422, 423, 404,
                             403
                                , 401, 402, 383, 382, 380, 381, 362, 361, 359, 360, 341, 340],
                            "Radius:=", self.parementer[67],
                            "Setback:=", "0mm"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:="	, "Rotor",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [342 ,589, 573, 568, 552, 547, 531, 526, 510, 505, 489, 484, 468, 463, 447, 442, 426, 421
                                , 405, 400, 384, 379, 363, 358],
                            "Radius:=", self.parementer[68],
                            "Setback:=", "0mm"
                        ]
                    ])
                oEditor.CreateCircle(
                    [
                        "NAME:CircleParameters",
                        "IsCovered:="	, True,
                        "XCenter:="		, "0mm",
                        "YCenter:="		, "0mm",
                        "ZCenter:="		, "0mm",
                        "Radius:="		, "12.777202686987mm",
                        "WhichAxis:="		, "Z",
                        "NumSegments:="		, "0"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "Circle1",
                        "Flags:="		, "",
                        "Color:="		, "(143 175 143)",
                        "Transparency:="	, 0,
                        "PartCoordinateSystem:=", "Global",
                        "UDMId:="		, "",
                        "MaterialValue:="	, "\"vacuum\"",
                        "SurfaceMaterialValue:=", "\"\"",
                        "SolveInside:="		, True,
                        "ShellElement:="	, False,
                        "ShellElementThickness:=", "0mm",
                        "IsMaterialEditable:="	, True,
                        "UseMaterialAppearance:=", False,
                        "IsLightweight:="	, False
                    ])
                oEditor.Copy(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Rotor"
                    ])
                oEditor.Paste()
                oEditor.Subtract(
                    [
                        "NAME:Selections",
                        "Blank Parts:="		, "Rotor1",
                        "Tool Parts:="		, "Circle1"
                    ],
                    [
                        "NAME:SubtractParameters",
                        "KeepOriginals:="	, False
                    ])
                oEditor.Subtract(
                    [
                        "NAME:Selections",
                        "Blank Parts:="		, "Rotor",
                        "Tool Parts:="		, "Rotor1"
                    ],
                    [
                        "NAME:SubtractParameters",
                        "KeepOriginals:="	, True
                    ])
                oModule = oDesign.GetModule("MeshSetup")
                oModule.AssignLengthOp(
                    [
                        "NAME:Length1",
                        "RefineInside:="	, True,
                        "Enabled:="		, True,
                        "Objects:="		, ["Rotor1"],
                        "RestrictElem:="	, False,
                        "NumMaxElem:="		, "1000",
                        "RestrictLength:="	, True,
                        "MaxLength:="		, self.parementer[61]
                    ])
                oModule.AssignLengthOp(
                    [
                        "NAME:Length2",
                        "RefineInside:="	, False,
                        "Enabled:="		, True,
                        "Edges:="		, [8],
                        "RestrictElem:="	, False,
                        "NumMaxElem:="		, "1000",
                        "RestrictLength:="	, True,
                        "MaxLength:="		, self.parementer[62]
                    ])
                oModule.AssignLengthOp(
                    [
                        "NAME:Length3",
                        "RefineInside:="	, False,
                        "Enabled:="		, True,
                        "Edges:="		, [1173 ,53, 1201, 52, 1202, 55, 1174, 1152, 41, 1180, 40, 1181, 43, 1153, 1159, 75, 1187, 74,
                         1160
                            , 77, 1188, 1166, 64, 1194, 63, 1195, 66, 1167],
                        "RestrictElem:=", False,
                        "NumMaxElem:=", "1000",
                        "RestrictLength:=", True,
                        "MaxLength:=", self.parementer[63]
                    ])
                oModule.AssignTrueSurfOp(
                    [
                        "NAME:SurfApprox1",
                        "Objects:=", ["Rotor1", "Mag_0", "Mag_2", "Mag_1", "Mag_3", "Band", "InnerRegion"],
                        "CurvedSurfaceApproxChoice:=", "ManualSettings",
                        "SurfDevChoice:=", 2,
                        "SurfDev:=", self.parementer[64],
                        "NormalDevChoice:=", 2,
                        "NormalDev:=", "3deg",
                        "AspectRatioChoice:=", 1
                    ])
                oProject.Save()
                oDesign.GenerateMesh(["Setup1"])
                oEditor.Move(
                    [
                        "NAME:Selections",
                        "Selections:=",
                        "Coil_0,Coil_1,Coil_2,Coil_3,Coil_4,Coil_5,Coil_6,Coil_7,Coil_8,Coil_9,Coil_10,Coil_11,CoilRe_0,CoilRe_1,CoilRe_2,CoilRe_3,CoilRe_4,CoilRe_5,CoilRe_6,CoilRe_7,CoilRe_8,CoilRe_9,CoilRe_10,CoilRe_11,Rotor,Rotor1,Band,InnerRegion,Shaft",
                        "NewPartsModelFlag:=", "Model"
                    ],
                    [
                        "NAME:TranslateParameters",
                        "TranslateVectorX:=", "0mm",
                        "TranslateVectorY:=", "0.02mm",
                        "TranslateVectorZ:=", "0mm"
                    ])
                oEditor.CreateRelativeCS(
                    [
                        "NAME:RelativeCSParameters",
                        "Mode:="	, "Euler Angle ZYZ",
                        "OriginX:="		, "0mm",
                        "OriginY:="		, "0.02mm",
                        "OriginZ:="		, "0mm",
                        "Psi:="			, "0deg",
                        "Theta:="		, "0deg",
                        "Phi:="			, "0deg"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "RelativeCS1"
                    ])
                oModule = oDesign.GetModule("ModelSetup")
                oModule.EditMotionSetup("MotionSetup1",
                                        [
                                            "NAME:Data",
                                            "Move Type:="		, "Rotate",
                                            "Coordinate System:="	, "RelativeCS1",
                                            "Axis:="		, "Z",
                                            "Is Positive:="		, True,
                                            "InitPos:="		, "-15deg",
                                            "HasRotateLimit:="	, False,
                                            "NonCylindrical:="	, False,
                                            "Consider Mechanical Transient:=", False,
                                            "Angular Velocity:="	, "3000rpm"
                                        ])
                oEditor.CreateCircle(
                    [
                        "NAME:CircleParameters",
                        "IsCovered:="		, True,
                        "XCenter:="		, "0mm",
                        "YCenter:="		, "0mm",
                        "ZCenter:="		, "0mm",
                        "Radius:="		, "14.59mm",
                        "WhichAxis:="		, "Z",
                        "NumSegments:="		, "0"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "Circle2",
                        "Flags:="		, "",
                        "Color:="		, "(143 175 143)",
                        "Transparency:="	, 0,
                        "PartCoordinateSystem:=", "Global",
                        "UDMId:="		, "",
                        "MaterialValue:="	, "\"vacuum\"",
                        "SurfaceMaterialValue:=", "\"\"",
                        "SolveInside:="		, True,
                        "ShellElement:="	, False,
                        "ShellElementThickness:=", "0mm",
                        "IsMaterialEditable:="	, True,
                        "UseMaterialAppearance:=", False,
                        "IsLightweight:="	, False
                    ])
                oEditor.CreateObjectFromEdges(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Circle2",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:BodyFromEdgeToParameters",
                            "Edges:="		, [2550]
                        ]
                    ],
                    [
                        "CreateGroupsForNewObjects:=", False
                    ])
                oEditor.ChangeProperty(
                    [
                        "NAME:AllTabs",
                        [
                            "NAME:Geometry3DAttributeTab",
                            [
                                "NAME:PropServers",
                                "Circle2_ObjectFromEdge1"
                            ],
                            [
                                "NAME:ChangedProps",
                                [
                                    "NAME:Model",
                                    "Value:="		, False
                                ]
                            ]
                        ]
                    ])
                oEditor.Delete(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Circle2"
                    ])

            else:
                oEditor.Chamfer(
                    [
                        "NAME:Selections",
                        "Selections:="	, "Mag_3,Mag_0,Mag_1,Mag_2",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:ChamferParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [80 ,81],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:="	, [],
                            "Vertices:="		, [47 ,46],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:="	, [],
                            "Vertices:="		, [59 ,58],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ],
                        [
                            "NAME:ChamferParameters",
                            "Edges:="	, [],
                            "Vertices:="		, [70 ,69],
                            "LeftDistance:=", self.parementer[65],
                            "RightDistance:=", self.parementer[65],
                            "ChamferType:=", "Symmetric"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:="	, "Mag_3,Mag_0,Mag_1,Mag_2",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [78 ,79],
                            "Radius:=", self.parementer[66],
                            "Setback:="	, "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [44 ,45],
                            "Radius:=", self.parementer[66],
                            "Setback:="	, "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [56 ,57],
                            "Radius:=", self.parementer[66],
                            "Setback:="	, "0mm"
                        ],
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [67 ,68],
                            "Radius:=", self.parementer[66],
                            "Setback:="	, "0mm"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Rotor",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [612 ,611, 592, 593, 591, 590, 571, 572, 570, 569, 550, 551, 549, 548, 529, 530, 528, 527
                                , 508, 509, 507, 506, 487, 488, 486, 485, 466, 467, 465, 464, 446, 445, 444, 443, 424,
                             425
                                , 423, 422, 403, 404, 402, 401, 382, 383, 381, 380, 655, 656, 654, 653, 634, 635, 633,
                             632
                                , 614, 613],
                            "Radius:=", self.parementer[67],
                            "Setback:="	, "0mm"
                        ]
                    ])
                oEditor.Fillet(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Rotor",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:FilletParameters",
                            "Edges:="		, [],
                            "Vertices:="		, [615 ,610, 594, 589, 573, 568, 552, 547, 531, 526, 510, 505, 489, 484, 468, 463, 447, 442
                                , 426, 421, 405, 400, 384, 673, 657, 652, 636, 631],
                            "Radius:=", self.parementer[68],
                            "Setback:="	, "0mm"
                        ]
                    ])
                oEditor.CreateCircle(
                    [
                        "NAME:CircleParameters",
                        "IsCovered:="		, True,
                        "XCenter:="		, "0mm",
                        "YCenter:="		, "0mm",
                        "ZCenter:="		, "0mm",
                        "Radius:="		, "12.8654184441361mm",
                        "WhichAxis:="		, "Z",
                        "NumSegments:="		, "0"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "Circle1",
                        "Flags:="		, "",
                        "Color:="		, "(143 175 143)",
                        "Transparency:="	, 0,
                        "PartCoordinateSystem:=", "Global",
                        "UDMId:="		, "",
                        "MaterialValue:="	, "\"vacuum\"",
                        "SurfaceMaterialValue:=", "\"\"",
                        "SolveInside:="		, True,
                        "ShellElement:="	, False,
                        "ShellElementThickness:=", "0mm",
                        "IsMaterialEditable:="	, True,
                        "UseMaterialAppearance:=", False,
                        "IsLightweight:="	, False
                    ])
                oEditor.Copy(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Rotor"
                    ])
                oEditor.Paste()
                oEditor.Subtract(
                    [
                        "NAME:Selections",
                        "Blank Parts:="		, "Rotor1",
                        "Tool Parts:="		, "Circle1"
                    ],
                    [
                        "NAME:SubtractParameters",
                        "KeepOriginals:="	, False
                    ])
                oEditor.Subtract(
                    [
                        "NAME:Selections",
                        "Blank Parts:="		, "Rotor",
                        "Tool Parts:="		, "Rotor1"
                    ],
                    [
                        "NAME:SubtractParameters",
                        "KeepOriginals:="	, True
                    ])
                oModule = oDesign.GetModule("MeshSetup")
                oModule.AssignLengthOp(
                    [
                        "NAME:Length1",
                        "RefineInside:="	, True,
                        "Enabled:="		, True,
                        "Objects:="		, ["Rotor1"],
                        "RestrictElem:="	, False,
                        "NumMaxElem:="		, "1000",
                        "RestrictLength:="	, True,
                        "MaxLength:="		, self.parementer[61]
                    ])
                oModule.AssignLengthOp(
                    [
                        "NAME:Length2",
                        "RefineInside:="	, False,
                        "Enabled:="		, True,
                        "Edges:="		, [8],
                        "RestrictElem:="	, False,
                        "NumMaxElem:="		, "1000",
                        "RestrictLength:="	, True,
                        "MaxLength:="		, self.parementer[62]
                    ])
                oModule.AssignLengthOp(
                    [
                        "NAME:Length3",
                        "RefineInside:="	, False,
                        "Enabled:="		, True,
                        "Edges:="		, [1317 ,77, 1345, 74, 1337, 64, 1365, 63, 1344, 75, 1316, 1324, 43, 1352, 40, 1351, 41, 1323, 55
                            , 1331, 1359, 52, 53, 1330, 1358, 66, 1338, 1366],
                        "RestrictElem:=", False,
                        "NumMaxElem:=", "1000",
                        "RestrictLength:=", True,
                        "MaxLength:="	, self.parementer[63]
                    ])
                oModule.AssignTrueSurfOp(
                    [
                        "NAME:SurfApprox1",
                        "Objects:="		, ["Rotor1" ,"Mag_0", "Mag_2", "Mag_1", "Mag_3", "Band", "InnerRegion"],
                        "CurvedSurfaceApproxChoice:=", "ManualSettings",
                        "SurfDevChoice:=", 2,
                        "SurfDev:=", "0.001mm",
                        "NormalDevChoice:=", 2,
                        "NormalDev:="	, "3deg",
                        "AspectRatioChoice:="	, 1
                    ])
                oProject.Save()
                oDesign.GenerateMesh(["Setup1"])
                oEditor.Move(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Coil_0,Coil_1,Coil_2,Coil_3,Coil_4,Coil_5,Coil_6,Coil_7,Coil_8,Coil_9,Coil_10,Coil_11,Coil_12,Coil_13,CoilRe_0,CoilRe_1,CoilRe_2,CoilRe_3,CoilRe_4,CoilRe_5,CoilRe_6,CoilRe_7,CoilRe_8,CoilRe_9,CoilRe_10,CoilRe_11,CoilRe_12,CoilRe_13,Rotor,Rotor1,Band,InnerRegion,Shaft",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:TranslateParameters",
                        "TranslateVectorX:="	, "0mm",
                        "TranslateVectorY:="	, "0.02mm",
                        "TranslateVectorZ:="	, "0mm"
                    ])
                oEditor.CreateRelativeCS(
                    [
                        "NAME:RelativeCSParameters",
                        "Mode:="		, "Euler Angle ZYZ",
                        "OriginX:="		, "0mm",
                        "OriginY:="		, "0.02mm",
                        "OriginZ:="		, "0mm",
                        "Psi:="			, "0deg",
                        "Theta:="		, "0deg",
                        "Phi:="			, "0deg"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "RelativeCS1"
                    ])
                oModule = oDesign.GetModule("ModelSetup")
                oModule.EditMotionSetup("MotionSetup1",
                                        [
                                            "NAME:Data",
                                            "Move Type:="		, "Rotate",
                                            "Coordinate System:="	, "RelativeCS1",
                                            "Axis:="		, "Z",
                                            "Is Positive:="		, True,
                                            "InitPos:="		, "-6.42857deg",
                                            "HasRotateLimit:="	, False,
                                            "NonCylindrical:="	, False,
                                            "Consider Mechanical Transient:=", False,
                                            "Angular Velocity:="	, "3000rpm"
                                        ])
                oEditor.CreateCircle(
                    [
                        "NAME:CircleParameters",
                        "IsCovered:="		, True,
                        "XCenter:="		, "0mm",
                        "YCenter:="		, "0mm",
                        "ZCenter:="		, "0mm",
                        "Radius:="		, "14.59mm",
                        "WhichAxis:="		, "Z",
                        "NumSegments:="		, "0"
                    ],
                    [
                        "NAME:Attributes",
                        "Name:="		, "Circle2",
                        "Flags:="		, "",
                        "Color:="		, "(143 175 143)",
                        "Transparency:="	, 0,
                        "PartCoordinateSystem:=", "Global",
                        "UDMId:="		, "",
                        "MaterialValue:="	, "\"vacuum\"",
                        "SurfaceMaterialValue:=", "\"\"",
                        "SolveInside:="		, True,
                        "ShellElement:="	, False,
                        "ShellElementThickness:=", "0mm",
                        "IsMaterialEditable:="	, True,
                        "UseMaterialAppearance:=", False,
                        "IsLightweight:="	, False
                    ])
                oEditor.CreateObjectFromEdges(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Circle2",
                        "NewPartsModelFlag:="	, "Model"
                    ],
                    [
                        "NAME:Parameters",
                        [
                            "NAME:BodyFromEdgeToParameters",
                            "Edges:="		, [2930]
                        ]
                    ],
                    [
                        "CreateGroupsForNewObjects:=", False
                    ])
                oEditor.ChangeProperty(
                    [
                        "NAME:AllTabs",
                        [
                            "NAME:Geometry3DAttributeTab",
                            [
                                "NAME:PropServers",
                                "Circle2_ObjectFromEdge1"
                            ],
                            [
                                "NAME:ChangedProps",
                                [
                                    "NAME:Model",
                                    "Value:="		, False
                                ]
                            ]
                        ]
                    ])
                oEditor.Delete(
                    [
                        "NAME:Selections",
                        "Selections:="		, "Circle2"
                    ])
            oDesign.SetDesignSettings(
                [
                    "NAME:Design Settings Data",
                    "Perform Minimal validation:=", False,
                    "EnabledObjects:=", [],
                    "PreserveTranSolnAfterDatasetEdit:=", False,
                    "ComputeTransientInductance:=", False,
                    "ComputeIncrementalMatrix:=", False,
                    "PerfectConductorThreshold:=", 1E+30,
                    "InsulatorThreshold:=", 1,
                    "ModelDepth:="	, "40mm",
                    "UseSkewModel:="	, False,
                    "EnableTranTranLinkWithSimplorer:=", False,
                    "BackgroundMaterialName:=", "vacuum",
                    "SolveFraction:="	, False,
                    "Multiplier:="		, "fractions"
                ],
                [
                    "NAME:Model Validation Settings",
                    "EntityCheckLevel:="	, "Strict",
                    "IgnoreUnclassifiedObjects:=", True,
                    "SkipIntersectionChecks:=", False
                ])
            oDesign.EnableHarmonicForceCalculation(
                [
                    "EnabledObjects:="	, ["Mag_0" ,"Mag_1", "Mag_2", "Mag_3"],
                    "ForceType:=", 1,
                    "WindowFunctionType:=", "Rectangular",
                    "NumberOfRepeatedSamples:=", "1",
                    "UseNumberOfLastCycles:=", True,
                    "NumberOfLastCycles:=", 1,
                    "StartTime:=", "0s",
                    "UseNumberOfCyclesForStopTime:=", True,
                    "NumberOfCyclesForStopTime:=", 1,
                    "StopTime:="	, "0.01s",
                    "OutputFreqRangeType:="	, "Use All"
                ])
            oModule = oDesign.GetModule("AnalysisSetup")
            oModule.EditSetup("Setup1",
                              [
                                  "NAME:Setup1",
                                  "Enabled:="	, True,
                                  [
                                      "NAME:MeshLink",
                                      "ImportMesh:="		, False
                                  ],
                                  "NonlinearSolverResidual:=", "0.0001",
                                  "TimeIntegrationMethod:=", "BackwardEuler",
                                  "SmoothBHCurve:="	, False,
                                  "StopTime:="		, "0.025s",
                                  "TimeStep:="		, "(60/3000/240) s",
                                  "OutputError:="		, False,
                                  "OutputPerObjectCoreLoss:=", False,
                                  "OutputPerObjectSolidLoss:=", False,
                                  "UseControlProgram:="	, False,
                                  "ControlProgramName:="	, " ",
                                  "ControlProgramArg:="	, " ",
                                  "CallCtrlProgAfterLastStep:=", False,
                                  "FastReachSteadyState:=", False,
                                  "AutoDetectSteadyState:=", False,
                                  "IsGeneralTransient:="	, True,
                                  "IsHalfPeriodicTransient:=", False,
                                  "SaveFieldsType:="	, "Every N Steps",
                                  "N Steps:="		, "1",
                                  "Steps From:="		, "0.005s",
                                  "Steps To:="		, "0.025s",
                                  "UseNonLinearIterNum:="	, False,
                                  "CacheSaveKind:="	, "Count",
                                  "NumberSolveSteps:="	, 1,
                                  "RangeStart:="		, "0s",
                                  "RangeEnd:="		, "0.1s",
                                  "UseAdaptiveTimeStep:="	, False,
                                  "InitialTimeStep:="	, "0.002s",
                                  "MinTimeStep:="		, "0.001s",
                                  "MaxTimeStep:="		, "0.003s",
                                  "TimeStepErrTolerance:=", 0.0001
                              ])
            oProject.Save()
            oDesign.Analyze("Setup1")
            oModule = oDesign.GetModule("FieldsReporter")
            oModule.EnterQty("B")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarX")
            oModule.AddNamedExpression("Br", "Fields")
            oModule.EnterQty("B")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarY")
            oModule.AddNamedExpression("Bt", "Fields")
            oModule.CopyNamedExprToStack("Br")
            oModule.CopyNamedExprToStack("Br")
            oModule.CalcOp("*")
            oModule.CopyNamedExprToStack("Bt")
            oModule.CopyNamedExprToStack("Bt")
            oModule.CalcOp("*")
            oModule.CalcOp("-")
            oModule.EnterScalar(1.25663706143592E-06)
            oModule.EnterScalar(2)
            oModule.CalcOp("*")
            oModule.CalcOp("/")
            oModule.AddNamedExpression("Fr", "Fields")
            oModule.CopyNamedExprToStack("Br")
            oModule.CopyNamedExprToStack("Bt")
            oModule.CalcOp("*")
            oModule.EnterScalar(1.25663706143592E-06)
            oModule.CalcOp("/")
            oModule.AddNamedExpression("Ft", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarX")
            oModule.EnterEdge("Mag_0")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Fr1", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarX")
            oModule.EnterEdge("Mag_0")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Fr2", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarX")
            oModule.EnterEdge("Mag_2")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Fr3", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarX")
            oModule.EnterEdge("Mag_3")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Fr4", "Fields")
            oModule.CopyNamedExprToStack("Fr1")
            oModule.CopyNamedExprToStack("Fr2")
            oModule.CopyNamedExprToStack("Fr3")
            oModule.CopyNamedExprToStack("Fr4")
            oModule.CalcOp("+")
            oModule.CalcOp("+")
            oModule.CalcOp("+")
            oModule.AddNamedExpression("Frall", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarY")
            oModule.EnterEdge("Mag_0")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Ft1", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarY")
            oModule.EnterEdge("Mag_1")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Ft2", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarY")
            oModule.EnterEdge("Mag_2")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Ft3", "Fields")
            oModule.EnterQty("EdgeForceDensity")
            oModule.XForm("Cylindrical", ["0mm", "0mm", "0mm"])
            oModule.CalcOp("ScalarY")
            oModule.EnterEdge("Mag_3")
            oModule.CalcOp("Integrate")
            oModule.AddNamedExpression("Ft4", "Fields")
            oModule.CopyNamedExprToStack("Ft1")
            oModule.CopyNamedExprToStack("Ft2")
            oModule.CopyNamedExprToStack("Ft3")
            oModule.CopyNamedExprToStack("Ft4")
            oModule.CalcOp("+")
            oModule.CalcOp("+")
            oModule.CalcOp("+")
            oModule.AddNamedExpression("Ftall", "Fields")
            oModule = oDesign.GetModule("ReportSetup")

            oModule.ExportToFile("Torque", r'{}/{}'.format(self.a, 'Torque.csv'), False)
            pg = self.image('Torque.csv')
            self.ui.graphicsView1.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')
            # # 设置坐标坐标轴标签
            # self.ui.graphicsView1.setLabel('left', 'LOSS')
            # # 设置底部坐标轴标签
            # self.ui.graphicsView1.setLabel('bottom', 'epoch')
            # self.ui.graphicsView1.showGrid(x=True, y=True, alpha=0.1)

            oModule.ExportToFile('Currents', r'{}/{}'.format(self.a, 'Currents.csv'), False)
            pg = self.image('Currents.csv')
            self.ui.graphicsView2.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

            oModule.ExportToFile("Induced Voltages", r'{}/{}'.format(self.a, 'Induced Voltages.csv'),
                                 False)
            pg = self.image('Induced Voltages.csv')
            self.ui.graphicsView3.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

            oModule.ExportToFile("Flux Linkages", r'{}/{}'.format(self.a, 'Flux Linkages.csv'), False)
            pg = self.image('Flux Linkages.csv')
            self.ui.graphicsView4.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

            # 计算FFT Torque
            if self.ui.radioButton28.isChecked():
                oModule = oDesign.GetModule("ReportSetup")
                oModule.UpdateTraces("Torque", ["Moving1.Torque"], "Setup1 : Transient", [],
                                     [
                                         "Time:=", ["0.005s", "0.025s"],
                                         "fractions:="	, ["Nominal"]
                                     ],
                                     [
                                         "X Component:="		, "Time",
                                         "Y Component:="		, ["Moving1.Torque"]
                                     ])
                oModule = oDesign.GetModule("Solutions")
                oModule.FFTOnReport("Torque", "Rectangular", "mag")
                oModule = oDesign.GetModule("ReportSetup")

                oModule.ExportToFile("FFT Torque", r'{}/{}'.format(self.a, 'FFT Torque.csv') ,False)
                pg = self.image('FFT Torque.csv')
                self.ui.graphicsView6.plot(pg.iloc[:, 0], pg.iloc[:, 2], pen='r')

            # 计算Frall
            if self.ui.radioButton30.isChecked():
                oModule = oDesign.GetModule("ReportSetup")
                oModule.CreateReport("Frall", "Fields", "Rectangular Plot", "Setup1 : Transient",
                                     [],
                                     [
                                         "Time:=", ["All"],
                                         "fractions:="	, ["Nominal"]
                                     ],
                                     [
                                         "X Component:="		, "Time",
                                         "Y Component:="		, ["Frall"]
                                     ])

                oModule.ExportToFile("Frall", r'{}/{}'.format(self.a ,'Frall.csv'), False)
                pg = self.image('Frall.csv')
                self.ui.graphicsView7.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')

            # 计算Ftall
            if self.ui.radioButton32.isChecked():
                oModule = oDesign.GetModule("ReportSetup")
                oModule.CreateReport("Ftall", "Fields", "Rectangular Plot", "Setup1 : Transient",
                                     [],
                                     [
                                         "Time:=", ["All"],
                                         "fractions:="	, ["Nominal"]
                                     ],
                                     [
                                         "X Component:="		, "Time",
                                         "Y Component:="		, ["Ftall"]
                                     ])
                oModule.ExportToFile("Ftall", r'{}/{}'.format(self.a, 'Ftall.csv') ,False)
                pg = self.image('Ftall.csv')
                self.ui.graphicsView8.plot(pg.iloc[:, 0], pg.iloc[:, 1], pen='r')
                # 设置坐标坐标轴标签
                self.ui.graphicsView8.setLabel('left', 'LOSS')
                # 设置底部坐标轴标签
                self.ui.graphicsView8.setLabel('bottom', 'epoch')
                self.ui.graphicsView8.showGrid(x=True, y=True)
            # 按钮调用
            oProject.Save()

            # os.system(r'taskkill /F /IM ansysedt.exe')
        except Exception as e:
            self.ui.textEdit_2.setText("计算出错")
            print(e)
            # os.system(r'taskkill /F /IM ansysedt.exe')

    # 最终放入计算程序中

    def image(self, name):
        pg = pd.read_csv(r'{}/{}'.format(self.a, name))
        return pg

    # oModule.ExportImageToFile("Torque", "{}/Torque.png".format(self.ui.textEdit.text()), 1397, 750)
    # def run(self):
    #     self.pix = QPixmap("2.gif")
    #     self.movie = QMovie("{}/Torque.png".format(self.ui.textEdit.text()))
    #     self.ui.label.setMovie(self.movie)
    #     if self.sender() == self.ui.pushButton:  # 两个按钮控制
    #         self.movie.start()
    #     else:
    #         self.movie.stop()
    #         self.ui.label.setPixmap(self.pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())
