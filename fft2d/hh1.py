import numpy as np
import pandas as pd
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
data = pd.read_csv('erwei.csv',header=None)
y = data.iloc[0:511,1]
y = np.array(y)
y1 = ['' for i in range(12000)]
for i in range(50):
    for j in range(240):
        y1[j+i*240] = y[j]
y1 = np.array(y1)

yy = fft(y1)
yreal = list(yy.real)               # 获取实数部分
yimag = yy.imag               # 获取虚数部分
ykk = ['' for i in range(240)]
ykk[0] = yreal[0]
for i in range(50,12000,50):
    c = int(i/50)
    ykk[c] = yreal[i]
ykk = np.array(ykk)