import pandas as pd
data = pd.read_csv('1.csv')
height = int(data.shape[0]/512)
graph=[[0 for j in range(512)] for i in range(241)]
graph[1][2] = 1

for i in range(height):
    for j in range(512):
        graph[i][j] = data.iloc[i*512+j,2]
data1 = pd.DataFrame(graph)
data1 = pd.DataFrame(data1.values.T, index=data1.columns, columns=data1.index)
data1.to_csv('erwei.csv',header=None,index=None)