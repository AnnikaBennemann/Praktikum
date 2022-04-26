import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import tools

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
<<<<<<< HEAD
print('sigmaNtb= ',sigmaNtb)


#Betastrahlung

d, t, N, Nerror, A, Aerror= np.genfromtxt('content/beta.txt', unpack=True)
R = d*1e-6 # Massenbelegung



print('a1 =', a1)
print('b1 =', b1)
||||||| b2875df
print('sigmaNtb= ',sigmaNtb)
=======
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
plt.ylabel(r'$\ln(A/A_0)$')
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
plt.ylabel(r'$\ln(A/A_0)$')
plt.xlabel(r'$d/\si{\meter}$')
plt.savefig('build/plot2.pdf')
>>>>>>> 44b90a7ed7eb9e5f200256ed82bd21715f6aeab7
