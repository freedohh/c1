import os, sys, clr
import pandas as pd
import numpy as np
from math import *

# 定义输出FFT_data的数据类型，0：幅值， 1：复数
data_type = 0


def dft(x, inverse=False):
    N = len(x)
    inv = -1 if not inverse else 1
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * e ** (inv * 2j * pi * k * n / N)
        if inverse:
            X[k] /= N
    return X


def dft2(x):
    y = [dft(a) for a in x]
    y = [dft(a) for a in zip(*y)]
    y = zip(*y)
    return y


def Compute(distance, time, data):
    distance = list(set(distance))  # set删除重复元素  distance空间距离
    distance.sort()  # sort 排序distance
    distance = distance[:-1]  # 删除distance的最后一位数字

    time = list(set(time))  # 同上
    time.sort()
    time = time[:-1]


    fft2_data = dft2(data)
    factor = len(time) * len(distance) / 2.0
    fft2_abs = [[abs(b) / factor for b in a] for a in fft2_data]
    fft2_abs[0][0] /= 2.0
    Order1 = 20
    Order2 = 120
    Outputs = [fft2_abs[(len(time) - int(Order1)) % len(time)][int(Order2)]]
    return Outputs


xx = pd.read_csv('1.csv')
distance = ['' for i in range(512)]
for i in range(512):
    distance[i] = xx.iloc[i, 1]
distance = np.array(distance)
time = np.linspace(0.005, 0.025, 241)
data = pd.read_csv('erwei.csv')
for i in data:
    print(i)
