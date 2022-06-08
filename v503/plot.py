import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

U, R, t0, tauf, tauff, tab, tabf  = np.genfromtxt('content/Werte.txt', unpack=True)

v0 = 0.5/t0
tauf= unp.uarray(tauf,tauff)
vauf= 0.5/tauf
tab= unp.uarray(tab,tabf)
vab= 0.5/tab


Bed = 2* v0 /(vab-vauf)


print('v0 = ', v0)
print('vauf = ', vauf)
print('vab = ', vab)
print('Bedingung = ', Bed)

#############Temperatur

T, Ohm= np.genfromtxt('content/Temperatur.txt', unpack=True)

def f (x, a, b,c):
    return a*x**2+b*x+c

params, cov = curve_fit(f,Ohm, T)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])

plt.figure(1)
plt.plot(Ohm, T, 'kx', label='Werte')
plt.plot(Ohm, f(Ohm, *params), 'b-', label='Ausgleichsfunktion')
plt.ylabel(r'T$\mathbin{/} \si{\celsius}$')
plt.xlabel(r'R $\mathbin{/} \si{\mega\ohm}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

Temp= 7.50 * R**2 - 50.97 *R + 97.37 
print('Temp = ', Temp)

eta= 0.0048 * Temp + 1.7268 
print('eta = ', eta)


#r_oel = np.sqrt(9 * visko_gemessen * v_0 / (2 * g * dichte_oel))???
#r_korrigiert = (np.sqrt((B / (2 * p))**2 + 9 * visko_gemessen * v_0 / (2 * g * dichte_oel)) - B / (2 * p))???
#q  = 4 * np.pi / 3 * dichte_oel * r_korrigiert**3 * g * 1 / E_feld ???



