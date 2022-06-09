import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import umath
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
from cmath import sqrt

U, R, t0, tauf, tauff, tab, tabf  = np.genfromtxt('content/Werte.txt', unpack=True)

v0 = 0.5/t0
tauf= unp.uarray(tauf,tauff)
vauf= 0.5/tauf
tab= unp.uarray(tab,tabf)
vab= 0.5/tab


Bed = 2* v0 /(vab-vauf)


print('v0 = ', v0)
print('vauf = ', vauf)
print('vab = ', vab)
print('Bedingung = ', Bed)

#############Temperatur

T, Ohm= np.genfromtxt('content/Temperatur.txt', unpack=True)

def f (x, a, b,c):
    return a*x**2+b*x+c

params, cov = curve_fit(f,Ohm, T)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])
 
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])

plt.figure(1)
plt.plot(Ohm, T, 'kx', label='Werte')
plt.plot(Ohm, f(Ohm, *params), 'b-', label='Ausgleichsfunktion')
plt.ylabel(r'T$\mathbin{/} \si{\celsius}$')
plt.xlabel(r'R $\mathbin{/} \si{\mega\ohm}$')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

Temp= 7.50 * R**2 - 50.97 *R + 97.37 
print('Temp = ', Temp)

eta= 0.0048 * Temp + 1.7268 
print('eta = ', eta)

d = ufloat(0.0076250 ,0.0000051) # [m]
dichte_luft = 1.1644        # näherungsweise
dichte_oel = 886     # [kg/m^3]
B = 6.17e-5    # [Pa/m]
p = 760       # [Pa]
s = 0.0005      # [m]

vab= np.delete(vab,[0,1,12,14,21])
vauf= np.delete(vauf,[0,1,12,14,21])
eta= np.delete(eta,[0,1,12,14,21])
E = U/d
#print('v = ',v)

print('r_oel :')
i = 0
while i < 20:
    r_oel = umath.sqrt(9 * eta[i] * (vab[i]-vauf[i]) / (2 * 9.81 * (dichte_oel-dichte_luft)))
    print(r_oel)
    i  += 1

print('q :')
i = 0
while i < 20:
    q = 3*np.pi*eta[i]*umath.sqrt((9*eta[i]*(vab[i]-vauf[i]))/(4*9.81*(dichte_oel-dichte_luft)))*((vab[i]+vauf[i])/E[i])
    print(q)
    i  += 1

x, r, rerr, q , qerr, q_korr, q_korrerr= np.genfromtxt('content/plotzeug.txt', unpack=True)
r= unp.uarray(r,rerr)
qe= unp.uarray(q, qerr)

eta_korr = eta*(1/(1+B/(p*r*10**(-6))))
print('eta_korr = ',eta_korr)

q_1= qe*(1+B/(p*r*10**(-6)))**(3/2)
print('q_korr = ', q_1)



plt.figure(2)
plt.errorbar(range(1, len(noms(q)) + 1), np.sort(noms(q)), yerr= qerr, fmt='rx', label='Werte mit Fehlern')
#plt.plot(range(1, len(noms(q)) + 1), np.sort(noms(q)), 'kx', label = r'Messdaten')
plt.ylabel(r'q $\mathbin{/} 10^{-19} \si{\coulomb}$')
plt.xlabel(r'Messungen')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')

q= np.sort(noms(q))/ 1.602
q_mittel = np.array([np.mean(q[0:5]), q[6], np.mean(q[7:8]), np.mean(q[9:12]), np.mean(q[13:14]), np.mean(q[15:16]), q[17], q[18], q[19]])
print('q_mittel = ',q_mittel)
print(np.argmin(abs(q / 1.602 - 1)))


plt.figure(3)
plt.errorbar(range(1, len(noms(q_korr)) + 1), np.sort(noms(q_korr)), yerr= q_korrerr, fmt='rx', label='Werte mit Fehlern')
#plt.plot(range(1, len(noms(q_korr)) + 1), np.sort(noms(q_korr)), 'kx', label = r'Messdaten')
plt.ylabel(r'q(korrigiert) $\mathbin{/} 10^{-19} \si{\coulomb}$')
plt.xlabel(r'Messungen')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot3.pdf')

q_korr= np.sort(noms(q_korr))/ 1.602
q_mittel = np.array([np.mean(q_korr[0:5]), q_korr[6], np.mean(q_korr[7:8]), np.mean(q_korr[9:12]), np.mean(q_korr[13:14]), np.mean(q_korr[15:16]), q_korr[17], q_korr[18], q_korr[19]])
print('q_mittel = ',q_mittel)
print(np.argmin(abs(q / 1.602 - 1)))