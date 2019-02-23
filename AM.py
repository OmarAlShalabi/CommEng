import numpy as np
import matplotlib.pyplot as plt


#Properties
BASE_F = 200
Carrier_F = int(input('Enter Carrier Frequency: '))
t = np.arange(40000)/(60*44100)
t2 = np.arange(40000)/(2)


#Signals

BASEBAND_SIGNAL = 1*np.cos(2* np.pi * BASE_F * t)
CARRIER_SIGNAL = 4*np.cos(2* np.pi* Carrier_F * t)
MODULATED_SIGNAL = (1 + .49*BASEBAND_SIGNAL)*CARRIER_SIGNAL


#Special signals
RECT = np.piecewise(t2, [t2 < 0, (t2 >= 0) & (t2 < 5000), t2 >= 5000], [lambda x: 0,
lambda x: 10000, lambda x: 0])

RAMP = np.piecewise(t2, [t2 < 0, (t2 >= 0) & (t2 < 5000), t2 >= 5000], [lambda x: 0,
lambda x: 2*x, lambda x: 0])



MODULATED_SIGNAL2 = RECT*CARRIER_SIGNAL
MODULATED_SIGNAL3 = RAMP*CARRIER_SIGNAL

#Plot

plt.subplot(3, 1, 1)
plt.title('Full Amplitude Modulation')
plt.plot(BASEBAND_SIGNAL)
plt.ylabel('Message signal')
#plt.xlim(-10**4,4*10**4)
plt.ylim(-2, 2)
plt.subplot(3, 1, 2)
plt.plot(CARRIER_SIGNAL)
#plt.xlim(-10**4,4*10**4)
plt.ylabel('Carrier signal')
plt.ylim(-4,4)
plt.subplot(3, 1, 3)
plt.plot(MODULATED_SIGNAL)
#plt.xlim(-10**4,4*10**4)
plt.ylabel('Modulated signal')
plt.ylim(-6, 6)
plt.show()
