import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def shift(arr, sa):
    temp = arr.copy()
    if sa < 0:
        for i in range (len(arr) - 1,0,-1):
             if temp[i] == 1:   
                temp[i - sa] = temp[i]
                temp[i] = 0          
    else:
        for i in range (len(temp) - sa - 1):
            temp[i] = temp[i+sa]

    return temp


def movingAvg(arr,m1,m2):
    final = []
    factor = m1 + m2 + 1

    for i in range(len(arr)):
        final.append(0.0)

    for i in range(-m1,m2 + 1):
        temp = shift(arr,i)
        for k in range(len(arr)):
            final[k] += temp[k]

    for i in range(len(final)):
        final[i] /= factor
    return final




x = np.linspace(1,20,20)
y = []

for i in range(20):
    
    y.append(0.0)

for i in range(7,11):
    y[i-1] = 1.

plt.subplot(2,1,1)
plt.stem(x,y)


final = movingAvg(y,1,2)
plt.subplot(2,1,2)
plt.stem(x,final)
plt.show()