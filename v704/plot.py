import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit


N0= 828
sigmaN0= 28.77
N0t= 828/900
sigmaN0t= 28.77/900

d , t, N, sigmaN = np.genfromtxt('content/WerteEisen.txt', unpack=True)
d = d*0.001
Nt= N/t 
sigmaNt=sigmaN/t
Nt0= Nt-N0t
sigmaNt0= sigmaNt-sigmaN0t

print('Nt= ',Nt)
print('sigmaNt= ',sigmaNt)

db , tb, Nb, sigmaNb = np.genfromtxt('content/WerteBlei.txt', unpack=True)
db = db*0.001
Ntb= Nb/tb 
sigmaNtb=sigmaNb/tb
Ntb0= Ntb-N0t
sigmaNtb0= sigmaNtb-sigmaN0t
print('Ntb= ',Ntb)
print('sigmaNtb= ',sigmaNtb)

def f(x, a, b):
   return a * x + b
plt.figure(1)
x_plot = np.linspace(0, 0.025)
params, covariance_matrix = curve_fit(f, d, np.log(Nt0))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Ausgleichsgerade', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.errorbar(d, np.log(Nt0), yerr=[np.log(Nt0+sigmaNt0)-np.log(Nt0), np.log(Nt0)-np.log(Nt0-sigmaNt0)], fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label='Fehlerbalken')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(d, np.log(Nt0), 'r.', label='Messwerte', markersize=4)
plt.legend()
plt.grid()
plt.ylabel(r'$\ln(A)$')
plt.xlabel(r'$d/\si{\meter}$')
plt.savefig('build/plot1.pdf')

plt.figure(2)
x_plot = np.linspace(0, 0.025)
params, covariance_matrix = curve_fit(f, db, np.log(Ntb0))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Ausgleichsgerade', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.errorbar(db, np.log(Ntb0), yerr=[np.log(Ntb0+sigmaNtb0)-np.log(Ntb0), np.log(Ntb0)-np.log(Ntb0-sigmaNtb0)], fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label='Fehlerbalken')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(db, np.log(Ntb0), 'r.', label='Messwerte', markersize=4)
plt.legend()
plt.grid()
plt.ylabel(r'$\ln(A)$')
plt.xlabel(r'$d/\si{\meter}$')
plt.savefig('build/plot2.pdf')


#Betastrahlung

d, t, N, Nerror, A, Aerror= np.genfromtxt('content/beta.txt', unpack=True)
R = d*1e-6 # Massenbelegung


def f(x, a, b):
   return a * x + b

plt.figure(3)
d_plot = np.delete(d,[6,7,8,9,10,11])
A_plot= np.delete(A,[6,7,8,9,10,11]) 
params, cov = curve_fit(f, d_plot, np.log(A_plot))
Aer= np.delete(Aerror,[6,7,8,9,10,11])

#plt.plot(d_plot, np.log(A_plot), 'r.', label='Messdaten',markersize=4)
plt.plot(d_plot, f(d_plot, *params), 'crimson', label='Ausgleichsgerade', linewidth=1.5)
errors = np.sqrt(np.diag(cov))
print('a1 =', params[0], '±', errors[0])
print('b1 =', params[1], '±', errors[1])
plt.errorbar(d_plot, np.log(A_plot), yerr=[np.log(A_plot+Aer)-np.log(A_plot), np.log(A_plot)-np.log(A_plot-Aer)], fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label='Messdaten mit Fehlerbalken')
#zweiter linie
d_plot2 = np.delete(d,[0,1,2,3,4,5])
A_plot2= np.delete(A,[0,1,2,3,4,5])
 #hier nochmal gucken, ob wir den einen drin lassen

params, cov = curve_fit(f, d_plot2, np.log(np.abs(A_plot2)))

plt.plot(d_plot2, np.log(np.abs( A_plot2)), 'b.', label='Messdaten')
plt.plot(d_plot2, f(d_plot2, *params), 'cyan', label='Ausgleichsgerade', linewidth=1.5)
plt.legend()
plt.grid()
plt.ylabel(r'$\ln(A/A_0)$')
plt.xlabel(r'$d/\si{\micro\meter}$')
plt.savefig('build/plot3.pdf')

print('a2 =', params[0], '±', errors[0])
print('b2 =', params[1], '±', errors[1])









