import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

#Magnetfeld Grafik
x, B = np.genfromtxt('content/Magnetfeld.txt', unpack=True)


plt.figure(1)
plt.plot(x, B,'rx', label='Messdaten')
plt.ylabel(r'$B / \si{\milli\tesla}$')
plt.xlabel(r'$x / \si{\centi\meter}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1.pdf') 

#effektive Masse bestimmen

#winkel normieren
lu,t1u, t2u  = np.genfromtxt('content/undotiert.txt', unpack=True)
l12,t112, t212  = np.genfromtxt('content/12.txt', unpack=True)
l28,t128, t228  = np.genfromtxt('content/28.txt', unpack=True)

#Wellenlänge berechnen
lm = np.mean(lu)

#l Größenordung anpassen
#lu = lu * 10**(-6)
#l12 = l12 * 10**(-6)
#l28 = l28 * 10**(-6)

#Dicke
du = 5.11 * 10**(-3)
d12 = 1.36 * 10**(-3)
d28 = 1.296 * 10**(-3)

tu = 1/2 * 1/du * np.abs(t1u-t2u) * np.pi/180
#print('tu =' , tu)
t12 = 1/2 * 1/d12 * np.abs(t112-t212) * np.pi/180
#print('t12 =' , t12)
t28 = 1/2 * 1/d28 * np.abs(t128-t228) * np.pi/180
#print('t28 =' , t28)

plt.figure(2)
plt.plot(lu**2, tu,'rx', label='Messdaten undotiert')
plt.xlabel(r'$\lambda ^2 / \si{\square\micro\meter}$')
plt.ylabel(r'$\theta / \si{\radian\per\meter}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot2.pdf') 

l12_plot= np.delete(l12, [7,8]) #DAtenpunkte löschen die hässlich sind
dt12= t12-tu
dt12_plot = np.delete(t12-tu,[7,8]) 

l28_plot= np.delete(l28, [7,8])
dt28 = t28-tu
dt28_plot= np.delete(t28-tu, [7,8])

#Fit
def fit(x ,a, b):
    return a*x+b

params1, cov1= curve_fit(fit, l12_plot**2, dt12_plot)
params2, cov2= curve_fit(fit,l28_plot**2, dt28_plot)
errors1 = np.sqrt(np.diag(cov1))
errors2 = np.sqrt(np.diag(cov2))

a1= ufloat(params1[0],errors1[0])
b1= ufloat(params1[1],errors1[1])
a2= ufloat(params2[0],errors2[0])
b2= ufloat(params2[1],errors2[1])
print('a1 =', params1[0], '±', errors1[0])
print('b1 =', params1[1], '±', errors1[1])
print('a2 =', params2[0], '±', errors2[0])
print('b2 =', params2[1], '±', errors2[1])

z = np.linspace(np.min(l12**2), np.max(l12**2), 500)
z2 = np.linspace(np.min(l28**2), np.max(l28**2), 500)

plt.figure(3)
plt.plot(l28_plot**2, dt28_plot,'bx', label='Messdaten dotiert, N_(2.8)')
plt.plot(z2, fit(z2,*params2),'b-', label='Regression dotiert, N_(2.8)')
plt.plot(l28[7]**2, dt28[7],color='darkcyan', marker='x')
plt.plot(l28[8]**2, dt28[8],color='darkcyan', marker='x')
plt.plot(l12_plot**2, dt12_plot,'ro', label='Messdaten dotiert, N_(1.2)')
plt.plot(z, fit(z,*params1),'r-', label='Regression dotiert, N_(1.2)')
plt.plot(l12[7]**2,dt12[7],color='orange',marker='o')
plt.plot(l12[8]**2,dt12[8],color='orange',marker='o')
plt.xlabel(r'$\lambda ^2 / \si{\square\micro\meter}$')
plt.ylabel(r'$\Delta \theta / \si{\radian\per\meter}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot3.pdf') 


#Variablen definieren
B = 435 *10**(-3)
N_12= 1.2*10**(18) *10**(6)
N_28= 2.8*10**(18) *10**(6)
n = 3.3


meff12 = unp.sqrt((const.e**3 * N_12 * B)/(a1*10**12* 8*np.pi**2 *const.epsilon_0 *const.c**3 * n ))/ const.m_e
meff28 = unp.sqrt((const.e**3 * N_28 * B)/(a2*10**12* 8*np.pi**2 *const.epsilon_0 *const.c**3 * n ))/ const.m_e
print('m*_12= ', meff12)
print('m*_28= ', meff28)
print('m*= ', 0.067* const.m_e)

meff12= ufloat(0.052,0.010)
meff28= ufloat(0.072,0.008)
abw12 = (meff12-0.067)/0.067*100
abw28 = (meff28-0.067)/0.067*100
print('abw12 = ', f'{abw12:.2f}')
print('abw28 = ', f'{abw28:.2f}')