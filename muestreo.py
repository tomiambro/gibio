import math
import numpy as np
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """ 
    
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """    

    # comienzo de la función
    tt = np.linspace(0, (N-1)/fs, N).flatten()
    signal = a0*np.sin(2*np.pi*f0*tt + p0)
    # fin de la función
    
    return tt, signal

def generador_ruido(fs, u, sigma, N, a0 = 1):
    tt = np.linspace(0, (N-1)/fs, N).flatten()
    signal = a0*np.random.normal(u, sigma, N)

    return tt, signal

#Script

fo = 10
fs = 1000
N = 2000

[t, s] = generador_senoidal(fs, fo, N)
[_, n] = generador_ruido(fs, 0, 0.1, N)

plt.subplot(311)
plt.plot(t, s)
plt.xlim(0, 1)
plt.subplot(312)
plt.plot(t, n)
plt.xlim(0, 1)
plt.subplot(313)
plt.plot(t, s+n)
plt.xlim(0, 1)
plt.show()