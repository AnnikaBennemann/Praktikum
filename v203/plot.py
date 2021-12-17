import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

T1, P1 = np.genfromtxt('content/untereinbar.txt', unpack=True)
T1= 273.15 + T1
P1= P1*10**5
P0= 102400000
x=T1

x_plot=1/T1
y_plot=np.log(P1/P0)
xfit = np.linspace(x_plot[0],x_plot[48],80)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)

#def f(m,x,b):
#    return m/x+b
#params, cov = curve_fit(f,T1,np.log(P1/P0))
errors = np.sqrt(np.diag(cov))

print('m =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

#x_plot = np.linspace(0,0.004,1000)
 
plt.figure(1)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit+params[1], 'k-', label='fit')
plt.ylabel(r'ln(p/p_0)')
plt.xlabel(r'$\frac{1}{\text{Temperatur}}\mathbin{/}\frac{1}{K}$')


plt.grid()
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')

#T2, P2 = np.genfromtxt('content/übereinbar.txt', unpack=True)
