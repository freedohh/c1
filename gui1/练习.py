#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 18:10
# @Author  : @linlianqin
# @Site    : 
# @File    : QDateTimeEdit_learn.py
# @Software: PyCharm
# @description:

from PyQt5.QtWidgets import QDateTimeEdit, QWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import QDateTime, QDate, QTime
import sys


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()

        layout = QVBoxLayout()
        # 同时显示日期时间
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())

        # 只显示日期
        dateTimeEdit3 = QDateTimeEdit(QDate.currentDate())
        # 只显示时间
        dateTimeEdit4 = QDateTimeEdit(QTime.currentTime())

        # 设置显示的格式
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        dateTimeEdit3.setDisplayFormat("yyyy.MM.dd")
        dateTimeEdit4.setDisplayFormat("HH:mm:ss")

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateTimeEdit3)
        layout.addWidget(dateTimeEdit4)

        self.setLayout(layout)

        # 默认将相应的日期或者时间返回
        dateTimeEdit1.dateChanged.connect(self.datechange)
        dateTimeEdit1.timeChanged.connect(self.timechange)
        dateTimeEdit1.dateTimeChanged.connect(self.datetimechange)

    def datechange(self, date):
        print(date)

    def timechange(self, time):
        print(time)

    def datetimechange(self, datetime):
        print(datetime)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DateTimeEditDemo()
    mainWin.show()
    sys.exit(app.exec_())