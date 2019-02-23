#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#input
array = list()
DFTarray = list()
n = input("Number of elements in the array: ")
for i in range(int(n)):
    n1 = input()
    array.append(n1)




#FFT
DFTarray = np.fft.fft(array)

#FFT array elements
for i in range(len(DFTarray)):
    print(DFTarray[i])


#Plot
N = int(len(DFTarray))*100
T = 1.0 / 100.0
x = np.linspace(0.0, N*T, N)
yf = DFTarray
xf = np.linspace(0.0, 1.0/(2.0*T), N//100)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()