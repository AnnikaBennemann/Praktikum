import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import norm 
import statistics 
from scipy.special import factorial


P, N, ch = np.genfromtxt('content/Werte1.txt', unpack=True)
p = P * 1e-3
p0 = 1013 * 1e-3
x0 = 1.7 * 1e-2

x = x0 * p / p0 *1e2
print(x)

E = 4 / 1023 * ch
print(E)

def f (x, m, b):
    return m*x+b
x_plot = np.delete(x,[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
N_plot= np.delete(N,[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
params, cov = curve_fit(f, x_plot, N_plot)
errors = np.sqrt(np.diag(cov))
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


plt.figure(1)
plt.plot(x, N, 'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Ausgleichsgerade')
#plt.plot(y, gerade(z, 0, 37247), 'm-', label=r'$\frac{N_0}{2}$')
plt.xlim(np.min(x)-0.5, np.max(x)+0.5)
plt.xlabel(r'$x \: / \: cm$')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot1.pdf')


########################################################

P2, N2, ch2 = np.genfromtxt('content/Werte2.txt', unpack=True)
p2 = P2 * 1e-3
p0 = 1013 * 1e-3
x0 = 3.0 * 1e-2

x2 = x0 * p2 / p0 *1e2
print(x2)

E2 = 4 / 1107 * ch2
print(E2)

def f (x2, m, b):
    return m*x2+b
x_plot2 = np.delete(x2,[0,1,2,3,4,5,6,7,8,9,12,13,14,18,19,20])
N_plot2= np.delete(N2,[0,1,2,3,4,5,6,7,8,9,12,13,14,18,19,20])
params, cov = curve_fit(f, x_plot2, N_plot2)
errors = np.sqrt(np.diag(cov))
 
print('a2 =', params[0], '±', errors[0])
print('b2 =', params[1], '±', errors[1])


plt.figure(2)
plt.plot(x2, N2, 'rx', label='Messdaten')
plt.plot(x_plot2, f(x_plot2, *params), 'b-', label='Ausgleichsgerade')
plt.plot(x2, f(x2, 0, 27774), 'm-', label=r'$\frac{N_0}{2}$')
plt.xlim(np.min(x2)-0.5, np.max(x2)+0.5)
plt.xlabel(r'$x \: / \: cm$')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot2.pdf')
############################################################################


def f (x, m, b):
    return m*x+b
x_plot =np.delete(x,[0,1,2,3,4,5,6,7,8,9,10,11])
E_plot= np.delete(E,[0,1,2,3,4,5,6,7,8,9,10,11])
params, cov = curve_fit(f, x_plot, E_plot)
errors = np.sqrt(np.diag(cov))
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


plt.figure(3)
plt.plot(x, E, 'rx', label='Messdaten')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Ausgleichsgerade')
#plt.plot(y, gerade(z, 0, 37247), 'm-', label=r'$\frac{N_0}{2}$')
plt.xlim(np.min(x)-0.5, np.max(x)+0.5)
plt.xlabel(r'$x \: / \: cm$')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot3.pdf')

######################################################################################

def f (x2, m, b):
    return m*x2+b
x_plot2 = np.delete(x2,[15,16,17,18,19,20])
E_plot2= np.delete(E2,[15,16,17,18,19,20])
params, cov = curve_fit(f, x_plot2, E_plot2)
errors = np.sqrt(np.diag(cov))
 
print('a2 =', params[0], '±', errors[0])
print('b2 =', params[1], '±', errors[1])


plt.figure(4)
plt.plot(x2, E2, 'rx', label='Messdaten')
plt.plot(x_plot2, f(x_plot2, *params), 'b-', label='Ausgleichsgerade')
#plt.plot(x2, f(x2, 0, 27774), 'm-', label=r'$\frac{N_0}{2}$')
plt.xlim(np.min(x2)-0.5, np.max(x2)+0.5)
plt.xlabel(r'$x \: / \: cm$')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot4.pdf')

##############################################################################

N = np.genfromtxt('content/Werte3.txt', unpack=True)

m = np.mean(N)
sigma = np.std(N)

print(m, sigma)
x=np.linspace(np.min(N),np.max(N),100)
plt.figure(5)
count, bins, ignored = plt.hist(N, 20, density=True, label='Messwerte')
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - m)**2 / (2 * sigma**2) ),linewidth=2, color='r', label='Gauß-Glocke')
plt.legend(loc='best')
plt.ylabel(r'absolute Häufigkeit')
plt.xlabel(r'N')
plt.savefig('build/gauss.pdf')

##################################################
#p = np.random.poisson(np.mean(N), 100)
#count, bins, ignored = plt.hist(p, 14, density=True)
m = np.min(N)
N = np.round(((N - m) / 100), decimals=0)
print(N)
print(m)

m = np.mean(N)
sigma = np.std(N)
print(m, sigma)



k = [0,1,2,3,4,5,6,7]
P = m**k / factorial(k, exact=False) * np.exp(-m)
P2 = [0.02, 0.06, 0.14, 0.24, 0.22, 0.25, 0.07, 0.00]
plt.figure(6)
plt.bar(k, P, color='b', width=-0.4, align='edge', label=r'Theoriewerte')
plt.bar(k, P2, color='c', width=0.4, align='edge', label=r'Messwerte')
plt.ylabel(r'$P_\lambda (k)$')
plt.xlabel(r'$k$')
plt.legend(loc='best')
plt.savefig('build/poisson.pdf')


###################################
m1=ufloat(-30827.55,2675.73)
b1= ufloat(196939.29,3843.14)
m2=ufloat(-47049.01, 3437.24)
b2=ufloat(115016.41,7165.45)

Nr1= 1/m1*(1023/2-b1)
Nr2= 1/m2*(1107/2-b2)
print('Nr1=',Nr1)
print('Nr2=',Nr2)

E1= (Nr1/3.1)**(2/3)
E2= (Nr2/3.1)**(2/3)

print('E1=', E1)
print('E2=', E2)