from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Input
FC = int( input("Enter Carrier frequency: "))


#Intialization
t = np.arange(44100)/(60*44100)
SQR = signal.square(2 * np.pi * 1000 * t)
Carrier = np.cos(2 * np.pi * FC * t)


#Phase modulation
MODULATED = np.cos(2 * np.pi * FC * t + SQR)



#Sub-Plot
#Message
plt.subplot(3, 1, 1)
plt.title('Phase Modulation')
plt.plot(SQR)
plt.ylabel('Message signal')

#Carrier
plt.subplot(3, 1, 2)
plt.plot(Carrier)
plt.ylabel('Carrier signal')


#Modulated
plt.subplot(3, 1, 3)
plt.plot(MODULATED)
plt.ylabel('Modulated signal')
plt.show()
