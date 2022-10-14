import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

T1, P1 = np.genfromtxt('content/untereinbar.txt', unpack=True)
T1= 273.15 + T1
P1= P1*10**2
P0= 102400
x=T1
R=8.314

x_plot=1/T1
y_plot=np.log(P1/P0)
xfit = np.linspace(x_plot[0],x_plot[48],80)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)

#def f(m,x,b):
#    return m/x+b
#params, cov = curve_fit(f,T1,np.log(P1/P0))
errors = np.sqrt(np.diag(cov))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
L= ufloat(-params[0]*R,errors[0]*R)
print('L =',L)
La= 373*R
Li= L-La
print('La=',La)
print('Li=',Li)
Lim= Li/96485
print('Li in eV =',Lim)

#x_plot = np.linspace(0,0.004,1000)
 
plt.figure(1)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit+params[1], 'k-', label='fit')
plt.ylabel(r'ln$(p/p_0)$')
plt.xlabel(r'$\frac{1}{T} \:/\: \frac{1}{\si{\kelvin}}$')


plt.grid()
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig('build/plot1.pdf')


P2, T2 = np.genfromtxt('content/übereinbar.txt', unpack=True)
T2= 273.15 + T2
P2= P2*10**5
P0= 102400
x=T2
R=8.314

x_plot=T2
y_plot=P2
xfit = np.linspace(x_plot[0],x_plot[28],80)
params, cov = np.polyfit(x_plot, y_plot, deg=3, cov=True)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])
print('d =', params[3], '±', errors[3])

plt.figure(2)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten')
plt.plot(xfit, params[0]*xfit**3+params[1]*xfit**2+params[2]*xfit+params[3], 'k-', label='fit')
plt.ylabel(r'$p \mathbin{/} \si{\pascal}$')
plt.xlabel(r'$T \mathbin{/} \si{\kelvin}$')

plt.grid()
plt.legend(loc='best')

plt.savefig('build/plot2.pdf')


def L(T2,a,b,c,d):
    return (((R*T2/2)+np.sqrt((R*T2/2)**2-0.9*(a*T2**3 + b*T2**2+c*T2+d)))*((3*a*T2**3+2*b*T2**2+c*T2)/(a*T2**3+b*T2**2+c*T2+d)))
def L2(T2,a,b,c,d):
    return (((R*T2/2)-np.sqrt((R*T2/2)**2-0.9*(a*T2**3 + b*T2**2+c*T2+d)))*((3*a*T2**3+2*b*T2**2+c*T2)/(a*T2**3+b*T2**2+c*T2+d)))

xfit = np.linspace(T2[0],T2[28],80)

plt.figure(3)
plt.plot(xfit, L(xfit, *params), 'r-', label='Genäherte Funktion für L')
plt.xlabel(r'$T \mathbin{/} \si{\kelvin}$')
plt.ylabel(r'$L \mathbin{/} \si{\joule\per\mol}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot3.pdf')

plt.figure(4)
plt.plot(xfit, L2(xfit, *params), 'r-', label='Genäherte Funktion für L')
plt.xlabel(r'$T \mathbin{/} \si{\kelvin}$')
plt.ylabel(r'$L \mathbin{/} \si{\joule\per\mol}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot4.pdf')

abw = (26100-40657)/40657
print('abw_1= ',abw)