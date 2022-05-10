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
a2 = A(vf30)
a3 = A(vf60)

plt.figure(1)
plt.errorbar(vf15, a1, fmt='r.', label=r'15$^{\circ}$')
plt.errorbar(vf30, a2, fmt='b.', label=r'30$^{\circ}$')
plt.errorbar(vf60, a3, fmt='g.', label=r'60$^{\circ}$')
plt.xlabel(r'Strömungsgeschwindigkeit [$\frac{m}{s}$]')
plt.ylabel(r'Δ$v / cos(\alpha)')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')


d , fmax , I = np.genfromtxt('content/Werte2.txt', unpack=True)

vfmax = F(fmax, 80.06)
print('vfmax= ', vfmax)

plt.figure(2)
plt.errorbar(d, vfmax, fmt='r.', label=r'Geschwindigkeit')
plt.errorbar(d, I, fmt='b.', label=r'Intensität')
plt.xlabel(r'Messtiefe [$\mu s$]')
plt.ylabel(r'I [$\frac{kV^2}{s}$] / $v$ [$\frac{m}{s}]')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
