import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 
 
x, y = np.loadtxt('runde.txt', unpack=True,delimiter=',')

z=(530*x**2-(x**3//3))*10**-6
 
def f(z,a,b):
    return a*z+b
params, cov = curve_fit(f, z, y)
errors = np.sqrt(np.diag(cov))
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x_plot = np.linspace(0,100,10)
 
plt.figure(1)
plt.plot(z, y,'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot,*params),'-', label='Linearer Fit')


plt.ylabel('$D(x)$ $[10^{-3} m]$')
plt.xlabel(r'$(Lx^2 - \frac{x^3}{3})$ $\left[10^{-3} m^3\right]$')
plt.grid()
plt.legend(loc='best')
 
 
plt.savefig('runde.pdf')