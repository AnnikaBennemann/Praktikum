import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 
 
x, y = np.loadtxt('rundb2.txt', unpack=True,delimiter=',')

z = (4*(x**3) - (12*550*x**2) + 9*(550**2*x)-(550**3))*10**-6
 
def f(z,a,b):
    return a*z+b
params, cov = curve_fit(f, z, y)
errors = np.sqrt(np.diag(cov))
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x_plot = np.linspace(40,175,10)
 
plt.figure(1)
plt.plot(z, y,'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot,*params),'-', label='Linearer Fit')


plt.ylabel('$D(x)$ $[10^{-3} m]$')
plt.xlabel(r'$(4x^3-12Lx^2+9L^2x-L^3)$ $\left[10^{-3} m^3\right]$')
plt.grid()
plt.legend(loc='best')
 
 
plt.savefig('rundb2.pdf')