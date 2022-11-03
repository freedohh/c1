import  numpy as np
import pandas as pd
def DFT2D(x, shift=True):
    '''
    Discrete space fourier transform
    x: Input matrix
    '''
    pi2 = 2*np.pi
    N1, N2 = x.shape
    X = np.zeros((N1, N2), dtype=np.complex64)
    n1, n2 = np.mgrid[0:N1, 0:N2]
    X.astype(float)
    for w1 in range(N1):
        for w2 in range(N2):
            j2pi = np.zeros((N1, N2), dtype=np.complex64)
            j2pi.imag = pi2*(w1*n1/N1 + w2*n2/N2)
            X[w1, w2] = np.sum(x*np.exp(-j2pi))
    if shift:
        X = np.roll(X, N1//2, axis=0)
        X = np.roll(X, N2//2, axis=1)
    return X
data = pd.read_csv('erwei.csv')
outputs = DFT2D(data)