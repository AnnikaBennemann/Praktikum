import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

theta2, imp1  = np.genfromtxt('content/bragg.txt', unpack=True)

theta = theta2 / 2

plt.figure(1)
plt.plot(theta, imp1, 'rx', label='Messdaten')
plt.ylabel(r'$Imp \mathbin{/} \si{\second}$)')
plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')
