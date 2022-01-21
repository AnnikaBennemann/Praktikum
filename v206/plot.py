import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

t, T2, pa, T1, pb, N = np.genfromtxt('content/Messung.txt', unpack=True)

t *= 60 #Zeit in Sekunden
T1 += 273.15 #Temperatur in Kelvin
T2 += 273.15
pa += 1 #Druck plus 1 bar 
pb += 1

#a

plt.figure(1)
plt.plot(t, T1, 'rx', label='T1')
plt.plot(t, T2, 'bx', label='T2')
plt.ylabel(r'Zeit $t \mathbin{/} \si{\second}$')
plt.xlabel(r'Temperatur $T \mathbin{/} \si{\kelvin}$')

plt.grid()
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')
