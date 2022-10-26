import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from numpy import exp
from numpy import sqrt
import scipy.constants as const
from uncertainties import ufloat_fromstr
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
import math
import scipy.constants as sc
from scipy import integrate


t, T, I= np.genfromtxt('content/Messung1.txt', unpack=True)
ta, Ta, Ia= np.genfromtxt('content/Messung1abzug.txt', unpack=True)

T=T+273.15 #Temperatur in K
Ta=Ta+273.15
#t=np.arange(0, 50)

#Mittlere Heizrate bestimmen
diff=np.diff(T)

print('Mittelwert Heizrate diff=', np.mean(diff), sem(diff))
H=ufloat(np.mean(diff),sem(diff))
print('Heizrate=', H)

######Plot/Fit Untergrung########
x = np.linspace(210, 316)
plt.plot (T, I,'r+', label='Messdaten')
plt.plot (Ta, Ia,'rx', label='Messdaten für Fit')

def fit(x ,a, b):
    return a*np.exp(-b/x)

params, cov= curve_fit(fit, Ta, Ia)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

plt.plot(x, fit(x,*params),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot1.pdf')
plt.show()

#Untergrund abziehen
Iohne=I-fit(T,*params)
print('I ohne Untergrund=',Iohne)
plt.plot(T, Iohne,'r+', label='Messdaten ohne Untergrund')
plt.plot(T[5:30], Iohne[5:30],'b+', label='Messdaten für Integral')
plt.plot(T[5:22], Iohne[5:22],'k+', label='Messdaten für Anlaufkurve')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot2.pdf')
plt.show()
