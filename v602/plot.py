import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

theta2, imp1  = np.genfromtxt('content/bragg.txt', unpack=True)

theta = theta2 / 2

plt.figure(1)
plt.plot(theta, imp1, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

thetae2, imp2  = np.genfromtxt('content/emission.txt', unpack=True)

thetae = thetae2 / 2
w1 = thetae [79:84]
R1= imp2 [79:84]
w2 = thetae [90:96]
R2= imp2 [90:96]


plt.figure(2)
plt.plot(thetae, imp2, 'b-', label='Bremsberg')
plt.plot(w1, R1, 'g-', label=r'$K_\alpha$')
plt.plot(w2, R2, 'r-', label=r'$K_\beta$')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')



thetaazink, imp3  = np.genfromtxt('content/zink_ab.txt', unpack=True)

plt.figure(3)
plt.plot(thetaazink, imp3, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot3.pdf')


thetastront, imp4  = np.genfromtxt('content/strontium_ab.txt', unpack=True)

plt.figure(4)
plt.plot(thetastront, imp4, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot4.pdf')


thetazirk, imp5  = np.genfromtxt('content/zirkonium_ab.txt', unpack=True)

plt.figure(5)
plt.plot(thetazirk, imp5, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot5.pdf')


thetabrom, imp6  = np.genfromtxt('content/brom_ab.txt', unpack=True)

plt.figure(6)
plt.plot(thetabrom, imp6, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot6.pdf')


thetagall, imp7  = np.genfromtxt('content/gallium_ab.txt', unpack=True)

plt.figure(7)
plt.plot(thetagall, imp7, 'b-', label='Messdaten')
plt.ylabel(r'Zählrate Impulse $ \mathbin{/} \si{\second}$')
plt.xlabel(r'Kristallwinkel $\theta \mathbin{/} \si{\degree}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot7.pdf')