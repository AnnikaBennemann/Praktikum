import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Strömungsgeschwindigkeiten berechnen
rpm , f15 , f30, f60 = np.genfromtxt('content/Werte1.txt', unpack=True)
alpha = np.array([ 80.06 , 70.57 , 54.74 ])
c = 1800
f = 2000000
def F(Frequenzverschiebung, Dopplerwinkel):
    return (Frequenzverschiebung * c) / (np.cos(Dopplerwinkel * (np.pi / 180)) * 2 * f)

vf15 = F(f15, 80.06)
vf30 = F(f30, 70.57)
vf60 = F(f60, 54.74)

print('vf15= ', vf15)
print('vf30= ', vf30)
print('vf60= ', vf60)

def A(x):
    return (x * 2 * f) / c

a1 = A(vf15)


plt.errorbar(vf15, a1, fmt='r.', label=r'Daten')
plt.xlabel(r'Strömungsgeschwindigkeit [$\frac{m}{s}$]')
plt.ylabel(r'Δ$v / cos(\alpha)')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

