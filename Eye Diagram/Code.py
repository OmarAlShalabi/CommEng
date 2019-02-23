import warnings
import numpy as np
import matplotlib.pyplot as plt


#Global variables
T = 2
Fs = 200
alpha = 0.5


#Get signal from Data
def get_signal(g,d):
    t = np.arange(-2*T,(len(d) + 2)*T, 1/Fs)
    g0 = g(np.array([1e-8]))
    xt = sum(d[k]*g(t-k*T) for k in range(len(d)))
    return t, xt/g0


# Filter implementation (RC)
def rc(t, beta):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return np.sinc(t)*np.cos(np.pi*beta*t)/(1-(2*beta*t)**2)

def getfilter(T,rolloff):
    return lambda t: rc(t/T,rolloff)



# AWGN Channel
def AWGN_channnel(signal,SNR):
    t = len(signal)
    noise = np.random.normal(0,1,t)
    signal_power = sum(np.abs(signal)*np.abs(signal))/t
    noise_power = sum(np.abs(noise)*np.abs(noise))/t
    K = (signal_power/noise_power) * 10 ** (-SNR/10)
    final_noise = np.sqrt(K)*noise
    return signal + final_noise


#Eye Diagram 
def drawFullEyeDiagram(xt):
    samples_perT = Fs*T
    samples_perWindow = 2*Fs*T
    parts = []
    startInd = 2*samples_perT
    
    for k in range(int(len(xt)/samples_perT) - 6):
        parts.append(xt[startInd + k*samples_perT + np.arange(samples_perWindow)])
    parts = np.array(parts).T
    
    t_part = np.arange(-T, T, 1/Fs)
    return t_part,parts


#Plotting the filter
t = np.arange(-3*T,3*T,1/Fs)
g = getfilter(T,alpha)
plt.plot(t,getfilter(T,alpha)(t))
plt.grid()
plt.show()


#Binary data
b_data = np.array([1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0])

#BPSK
b_modulated = 2*b_data - 1


#Signal Plot
t,xt = get_signal(g,b_modulated)
plt.plot(t,xt)
plt.grid()
plt.show()



#Noisy Signal plot
xn = AWGN_channnel(xt,31)
plt.plot(t,xn)
plt.grid()
plt.show()


#Eye Diagram
t_eye,xn_eye = drawFullEyeDiagram(xn)
plt.plot(t_eye,xn_eye,'b-')
plt.grid()
plt.show()

