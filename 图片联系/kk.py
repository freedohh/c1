import pandas as pd
import numpy as np
cc = pd.read_csv('Torque.csv')
k = cc.shape[0]
print(cc.iloc[:,0])