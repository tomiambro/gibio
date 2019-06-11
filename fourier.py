from pandas import DataFrame
from IPython.display import HTML
import numpy as np
# import scipy.fftpack
from generadores import generador_senoidal
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

#######################################
# Tu simulación que genere resultados #
#######################################
N = 1000
fs = 1000
fo = fs/4
fd = [0,0.01,0.25,0.5]

ts = 1/fs # tiempo de muestreo
df = fs/N # resolución espectral

ff = np.linspace(-N/2, (N/2)*df, N).flatten()


[tt, s0] = generador_senoidal(fs, fo + fd[0], N)
[_, s1] = generador_senoidal(fs, fo + fd[1], N)
[_, s2] = generador_senoidal(fs, fo + fd[2], N)
[_, s3] = generador_senoidal(fs, fo + fd[3], N)

S0 = np.fft.fft(s0)/N
S1 = np.fft.fft(s1)/N
S2 = np.fft.fft(s2)/N
S3 = np.fft.fft(s3)/N
M0 = (fo + fd[0]) * N / fs
M1 = (fo + fd[1]) * N / fs
M2 = (fo + fd[2]) * N / fs
M3 = (fo + fd[3]) * N / fs



tus_resultados = [ ['$ \lvert X(f_0) \lvert$', '$ \lvert X(f_0+1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                   ['',                        '',                           '$F:f \neq f_0$'], 
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', '']  # <-- acá debería haber numeritos :)
                 ]


tus_resultados[2][0] = np.abs(S0[int(M0)])
tus_resultados[3][0] = np.abs(S1[int(M1)])
tus_resultados[4][0] = np.abs(S1[int(M1)])
tus_resultados[5][0] = np.abs(S1[int(M1)])

tus_resultados[2][1] = np.abs(S0[int(M0 + 1)])
tus_resultados[3][1] = np.abs(S1[int(M1 + 1)])
tus_resultados[4][1] = np.abs(S1[int(M1 + 1)])
tus_resultados[5][1] = np.abs(S1[int(M1 + 1)])
for x in ff:
  tus_resultados[2][2] = np.power(np.abs(S0[int(x)]), 2)
  tus_resultados[3][2] = np.power(np.abs(S1[int(x)]), 2)
  tus_resultados[4][2] = np.power(np.abs(S1[int(x)]), 2)
  tus_resultados[5][2] = np.power(np.abs(S1[int(x)]), 2)


df = DataFrame(tus_resultados, columns=['Frecuencia central', 'Primer adyacente', 'Resto de frecuencias'],
               index=['$f_0$ \ expr. matemática', 
                      '', 
                      '$f_S/4$', 
                      '$f_S/4+0.01$', 
                      '$f_S/4+0.25$', 
                      '$f_S/4+0.5$'])
HTML(df.to_html())