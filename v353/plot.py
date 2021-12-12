import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
te, U_ce = np.genfromtxt('content/Entladekurve.txt', unpack=True)

def f(te,a,b):
    return a*te+b
params, cov = curve_fit(f,te,np.log(U_ce))
errors = np.sqrt(np.diag(cov))

a=ufloat(params[0], errors[0])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('Ln(U_C/U_0)=',np.log(U_ce))
print(a)
print('RC=',-1/a)

x_plot = np.linspace(0,4.4,300)
plt.figure(1)
plt.plot(te, np.log(U_ce),'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot,*params),'-', label='Linearer Fit')


plt.ylabel(r'$ln\Biggl(\frac{U_C}{U_0}\Biggr)$')
plt.xlabel(r'$t / \si{\milli\second}$')
plt.grid()
plt.legend(loc='best')
 
 
plt.savefig('build/Entladekurve.pdf') 


#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
f, U_c , t = np.genfromtxt('content/Werte.txt', unpack=True)
U_0=9
#ts=t*10**-3 # zeit in s
phase= t*f*360*10**-3
print('Phasendifferenz=',phase)

def g(f,A):
    return 1/(np.sqrt(1+(2*np.pi*f)**2*A**2))
params, cov = curve_fit(g,f,U_c/U_0)
errors = np.sqrt(np.diag(cov))
A= ufloat(params[0], errors[0])*10**3

print('A =', A)

x=np.linspace(20,20000,10000)
plt.figure(2)
plt.plot(f, U_c/U_0,'rx', label='Messdaten')
plt.plot(x, g(x,*params),'-', label='Fit')

plt.xscale('log')
plt.ylabel(r'$U_C \mathbin{/} U_0)$')
plt.xlabel(r'$f \mathbin{/} \si{\hertz}$')
plt.grid()
plt.legend(loc='best')
 
 
plt.savefig('build/SpannungFrequenz.pdf')



def phi(f,AR,b):
    return b*np.arctan(AR*2*np.pi*f)
params, cov = curve_fit(phi,f,phase)
errors = np.sqrt(np.diag(cov))
AR= ufloat(params[0], errors[0])*10**3

print('RC=',AR)
plt.figure(3)
plt.plot(f, phase ,'rx',label='Messdaten')
plt.plot(x, phi(x,*params),'-', label='Fit')

plt.xscale('log')
plt.ylabel(r'$\phi \mathbin{/} \si{\degree}$')
plt.xlabel(r'$f \mathbin{/} \si{\hertz}$')
plt.grid()
plt.legend(loc='best')
 

plt.savefig('build/PhaseFrequenz.pdf')

#polarplot
print(U_c/U_0)
A=U_c/9

a = np.linspace(0,np.pi/2,200)
plt.polar(phase/360*2*np.pi, A, 'rx', label='Messwerte')
plt.polar(a, np.cos(a), 'k-', label='Theoriekurve')
plt.legend(loc='best')
plt.tight_layout



plt.savefig('build/Polar.pdf')