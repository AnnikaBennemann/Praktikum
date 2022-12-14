import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Streuparameter plot


r00, I00 = np.genfromtxt('content/TEM00.txt', unpack=True)

r00= r00 * 10**-2   #Abstand in Meter
I00= I00 * 10**-6  #Intensität in Watt

def Tem0(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) #Ausgleichsfunktion TEM00

params1, cov1= curve_fit(Tem0, r00, I00)
errors1 = np.sqrt(np.diag(cov1))
I01= ufloat(params1[0],errors1[0])
r01= ufloat(params1[1],errors1[1])
w01= ufloat(params1[2],errors1[2])

plt.figure(1)
plt.plot(r00, I00, 'rx',label='Messwerte')
plt.plot(r00, Tem0(r00,*params1),'-', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM00.pdf')