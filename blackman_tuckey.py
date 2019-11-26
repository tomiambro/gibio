# -*- coding: utf-8 -*-
""" Imports """
import numpy as np
from scipy import signal as sig
from spectrum import CORRELOGRAMPSD
import matplotlib.pyplot as plt
import scipy.io as sio
""" General configs """
def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

fs = 1000
mat_struct = sio.loadmat('./ECG_TP4.mat')

zonas_con_interf_baja_frec = ( 
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        )

zonas_sin_interf = ( 
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        [4000, 5500], # muestras
        [10e3, 11e3],) # muestras

inf = int(zonas_con_interf_baja_frec[0][0])
sup = int(zonas_con_interf_baja_frec[0][1])


ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
N = len(ecg_one_lead)

inf = int(zonas_sin_interf[0][0])
sup = int(zonas_sin_interf[0][1])
N = sup - inf



f_w, psd_w = sig.welch(ecg_one_lead[inf:sup], fs=fs, nperseg=N/8, axis=0)
print(np.max(ecg_one_lead))

psd_w /= np.max(ecg_one_lead)

# psd_bt = CORRELOGRAMPSD(ecg_one_lead[inf:sup].flatten(), lag=int(N/8))

area = np.trapz(psd_w, axis=0)
interes = area * 0.95


f_i = np.array((f_w >= 0.66).nonzero()).flatten()
aux = psd_w[f_i].cumsum()



print(np.max(np.where(aux <= interes)))
i = np.max(np.where(aux <= interes))
print(f_w[f_i[i]])

plt.figure(1)
plt.xlabel('Muestras')
plt.plot(ecg_one_lead[inf:sup])
plt.grid()
plt.show()

plt.figure(2)
plt.xlabel('Frecuencia')
plt.semilogx(f_w, psd_w)
plt.grid(which='both', axis='both')
plt.show()

"""
plt.figure(3)
plt.xlabel('Frecuencia')
plt.plot(psd_bt)
plt.grid(which='both', axis='both')
plt.show()
"""