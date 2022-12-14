import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Streuparameter plot



##################################################################################TEM00

r00, I00 = np.genfromtxt('content/TEM00.txt', unpack=True)

#r00= r00 * 10**-2   #Abstand in Meter
I00 = I00+0.21      #Grundintensität abziehen
#I00= I00 * 10**-6  #Intensität in Watt

def Tem0(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) #Ausgleichsfunktion TEM00

params1, cov1= curve_fit(Tem0, r00, I00)
errors1 = np.sqrt(np.diag(cov1))
I01= ufloat(params1[0],errors1[0])
r01= ufloat(params1[1],errors1[1])
w01= ufloat(params1[2],errors1[2])

print('I01 =', params1[0], '±', errors1[0])
print('r01 =', params1[1], '±', errors1[1])
print('w01 =', params1[2], '±', errors1[2])

z = np.linspace(np.min(r00), np.max(r00), 500)

plt.figure(1)
plt.plot(r00, I00, 'rx',label='Messwerte')
plt.plot(z, Tem0(z,*params1),'-', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM00.pdf')

##################################################################################TEM10

r10, I10 = np.genfromtxt('content/TEM10.txt', unpack=True)

I10 = I10+0.21      #Grundintensität abziehen


def Tem1(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) * (8*(x-r0)**2)/w**2 #Ausgleichsfunktion TEM10

params2, cov2= curve_fit(Tem1, r10, I10)
errors2 = np.sqrt(np.diag(cov2))
I02= ufloat(params2[0],errors2[0])
r02= ufloat(params2[1],errors2[1])
w02= ufloat(params2[2],errors2[2])

print('I02 =', params2[0], '±', errors2[0])
print('r02 =', params2[1], '±', errors2[1])
print('w02 =', params2[2], '±', errors2[2])

z2 = np.linspace(np.min(r10), np.max(r10), 500)

plt.figure(2)
plt.plot(r10, I10, 'rx',label='Messwerte')
plt.plot(z2, Tem1(z2,*params2),'-', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM10.pdf')


##################################################################################TEM20

r20, I20 = np.genfromtxt('content/TEM20.txt', unpack=True)

I20 = I20+0.21      #Grundintensität abziehen


def Tem2(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) *( (64 *(x-r0)**4)/w**4 -(32*(x-r0)**2)/w**2 +4)#Ausgleichsfunktion TEM20

params3, cov3= curve_fit(Tem2, r20, I20) #passt irgendwie noch nciht so ganz
errors3 = np.sqrt(np.diag(cov3))
I03= ufloat(params3[0],errors3[0])
r03= ufloat(params3[1],errors3[1])
w03= ufloat(params3[2],errors3[2])

print('I03 =', params3[0], '±', errors3[0])
print('r03 =', params3[1], '±', errors3[1])
print('w03 =', params3[2], '±', errors3[2])

z3 = np.linspace(np.min(r20), np.max(r20), 500)

plt.figure(3)
plt.plot(r20, I20, 'rx',label='Messwerte')
plt.plot(z3, Tem2(z3,*params3),'-', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM20.pdf')