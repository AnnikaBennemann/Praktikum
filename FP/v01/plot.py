import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit


tv, n = np.genfromtxt('content/verzögerung.txt', unpack=True)
tv

def fit(x ,a, b):
    return a*x+b

params1, cov1= curve_fit(fit, tv[0:10], n[0:10])
params2, cov2= curve_fit(fit, tv[34:44], n[34:44])
errors1 = np.sqrt(np.diag(cov1))
errors2 = np.sqrt(np.diag(cov2))
print('a1 =', params1[0], '±', errors1[0])
print('b1 =', params1[1], '±', errors1[1])
print('a2 =', params2[0], '±', errors2[0])
print('b2 =', params2[1], '±', errors2[1])

plt.plot(tv[0:10], fit(tv[0:10],*params1),'-', label='Regression für Anstieg')
plt.plot(tv[34:44], fit(tv[34:44],*params2),'b-', label='Regression für Abfall')

plt.figure(1)
plt.plot(tv, n, 'rx',label='Messwerte')
plt.xlabel(r'counts $n$')
plt.ylabel(r'$\Delta t \mathbin{/} \unit{\nano\second}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/plot1.pdf')


x= (params2[1]-params1[1])/(params1[0]-params2[0])
print('Schnittpunkt also Verzögerung einstellen auf ', x)


tk, K= np.genfromtxt('content/channel.txt', unpack=True)
params3, cov3= curve_fit(fit, tk, K)
errors3 = np.sqrt(np.diag(cov3))
print('a3 =', params3[0], '±', errors3[0])
print('b3 =', params3[1], '±', errors3[1])

plt.figure(2)
plt.plot(tk, K, 'rx',label='Messwerte')
plt.plot(tk, fit(tk,*params3),'-', label='Regressionsgerade')
plt.ylabel(r'Channel')
plt.xlabel(r'$t \mathbin{/} \unit{\micro\second}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/plot2.pdf')
