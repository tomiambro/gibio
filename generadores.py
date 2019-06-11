import numpy as np
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