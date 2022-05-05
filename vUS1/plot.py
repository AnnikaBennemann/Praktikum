import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

t , t2, h = np.genfromtxt('content/plot1.txt', unpack=True)

x_plot=t
y_plot= 2*h
xfit = np.linspace(20,x_plot[3],20)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))
a= ufloat(params[0], errors[0])
b= ufloat(params[1], errors[1])
print(f'a {a:.5f}')
print(f'b {b:.5f}')

plt.figure(1)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit+params[1], 'b-', label='Ausgleichsgerade')
plt.ylabel(r'$d * 2 \mathbin{/} \si{\milli\meter}$')
plt.xlabel(r'$t \mathbin{/} \si{\micro\second}$')
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

A = np.genfromtxt('content/plot2.txt', unpack=True)
A0=1.18
x_plot=h
y_plot= np.log(A/A0)
xfit = np.linspace(10,120,100)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))
d= ufloat(params[0], errors[0])
f= ufloat(params[1], errors[1])
print(f'd {d:.5f}')
print(f'f {f:.5f}')

plt.figure(2)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit+params[1], 'b-', label='Ausgleichsgerade')
plt.ylabel(r'$\log{\frac{A}{A_0}}$')
plt.xlabel(r'$d \mathbin{/} \si{\milli\meter}$')
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')

x_plot=t2
y_plot= h
xfit = np.linspace(5,x_plot[3],50)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))
a= ufloat(params[0], errors[0])
b= ufloat(params[1], errors[1])
print(f'a {a:.5f}')
print(f'b {b:.5f}')

plt.figure(3)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit+params[1], 'b-', label='Ausgleichsgerade')
plt.ylabel(r'$d \mathbin{/} \si{\milli\meter}$')
plt.xlabel(r'$t \mathbin{/} \si{\micro\second}$')
plt.legend(loc='best')
plt.savefig('build/plot3.pdf')