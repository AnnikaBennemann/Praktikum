import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

Uge, Ige  = np.genfromtxt('content/gelb.txt', unpack=True)

plt.figure(1)
plt.plot(Uge, np.sqrt(Ige), 'yx', label='Messdaten')
plt.ylabel(r'$\sqrt(I) \mathbin{/} \sqrt(\si{\nano\ampere})$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot.pdf')
