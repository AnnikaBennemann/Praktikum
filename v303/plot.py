import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

phase , amp , ampn = np.genfromtxt('content/Amplitude.txt', unpack=True)

amp= amp/2
ampn= ampn/2 


def phi(phase,a,b,c):
    return 2/np.pi*a*np.cos(b*phase*2*np.pi/360)+c

params, cov = curve_fit(phi,phase,amp) 
errors = np.sqrt(np.diag(cov))
U_out= ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])

x=np.linspace(0,360,500)
U_0=U_out*np.pi/2

print('Uout=',U_out)
print('U_0=',U_0)
print('b=',b)
print('c=',c)

plt.figure(1)
plt.plot(phase, amp,'rx', label='Messdaten')
plt.plot(x, phi(x, *params),'-', label='Fit')
plt.xlabel(r'$\Phi \mathbin{/} \unit{\degree}$')
plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')

params, cov = curve_fit(phi,phase,ampn) 
errors = np.sqrt(np.diag(cov))
U_out= ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])

x=np.linspace(0,360,500)
U_0=U_out*np.pi/2

print('Uout=',U_out)
print('U_0=',U_0)
print('b=',b)
print('c=',c)

plt.figure(2)
plt.plot(phase, ampn,'rx', label='Messdaten')
plt.plot(x, phi(x, *params),'-', label='Fit')
plt.xlabel(r'$\Phi \mathbin{/} \unit{\degree}$')
plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
plt.legend(loc='best')

plt.savefig('build/plot2.pdf')


abst, U = np.genfromtxt('content/Diode.txt', unpack=True)
abst2, U2 = np.genfromtxt('content/Diode2.txt', unpack=True)

def f(abst2,a,b):
    return a*1/abst2+b

params, cov = curve_fit(f,abst2,U2) 
errors = np.sqrt(np.diag(cov))
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('a=',a)
print('b=',b)

x_plot=np.linspace(25,150,500)

plt.figure(3)
plt.plot(abst, U,'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot, *params),'-', label='Fit')
plt.xlabel(r'$x \mathbin{/} \unit{\centi\meter}$')
plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
plt.legend(loc='best')

plt.savefig('build/plot3.pdf')