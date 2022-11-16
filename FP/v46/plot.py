import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Magnetfeld Grafik
x, B = np.genfromtxt('content/Magnetfeld.txt', unpack=True)


plt.figure(1)
plt.plot(x, B,'rx', label='Messdaten')
plt.ylabel(r'$B / \si{\milli\tesla}$')
plt.xlabel(r'$x / \si{\centi\meter}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/Magnetfeld.pdf') 

#effektive Masse bestimmen

#winkel normieren
lu,t1u, t2u  = np.genfromtxt('content/undotiert.txt', unpack=True)
l12,t112, t212  = np.genfromtxt('content/12.txt', unpack=True)
l28,t128, t228  = np.genfromtxt('content/28.txt', unpack=True)

#Dicke
du = 1

t1u = t1u/ 