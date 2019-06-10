import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Insertar aquí el código para inicializar tu notebook
########################################################
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


# NO modifiques este bloque
############################

N  = 1000 # muestras
fs = 1000 # Hz

##################
# a.0) Senoidal #
#################

a0 = 1 # Volts
p0 = 0 # radianes
f0 = 10   # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################
[t, s0] = generador_senoidal(fs, f0, N)
plt.subplot(411)
plt.plot(t, s0, label="Sin 0")
plt.xlim(0, 1)
plt.ylabel('amplitud [V]')
plt.xlabel('tiempo [segundos]')
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.22, 1., .102), loc=1, ncol=1)

##################
# a.1) Senoidal #
#################

a1 = 1 # Volts
p1 = 0 # radianes
f1 = fs/2   # Hz
# f1 = 400   # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################

[_, s1] = generador_senoidal(fs, f1, N)

plt.subplot(412)
plt.plot(t, s1, label="Sin 1")
plt.xlim(0, 1)
plt.ylabel('amplitud [V]')
plt.xlabel('tiempo [segundos]')
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 0.3, 1., .102), loc=1, ncol=1)

##################
# a.2) Senoidal #
#################

a2 = 1       # Volts
p2 = np.pi/2 # radianes
f2 = fs/2    # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################

[_, s2] = generador_senoidal(fs, f2, N, a2, p2)

plt.subplot(413)
plt.plot(t, s2, label="Sin 2")
plt.xlim(0, 0.1)
plt.ylabel('amplitud [V]')
plt.xlabel('tiempo [segundos]')
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 0.3, 1., .102), loc=1, ncol=1)


##################
# a.3) Senoidal #
#################

a3 = 1     # Volts
p3 = 0     # radianes
f3 = fs+10 # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################

[_, s3] = generador_senoidal(fs, f3, N)

plt.subplot(414)
plt.plot(t, s3, label="Sin 3")
plt.xlim(0, 1)
plt.ylabel('amplitud [V]')
plt.xlabel('tiempo [segundos]')
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 0.3, 1., .102), loc=1, ncol=1)

plt.show()