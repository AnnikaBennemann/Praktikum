import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit


U ,I, N=np.genfromtxt('content/Werte.txt', unpack=True)
t= 60
N = N/t

dN = np.sqrt(N) #Weil Poissonveteilt

print('N = ', N, dN)
#Up = U[5:-7]
#Np = N[5:-7]

params, covariance_matrix = np.polyfit(U, N, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))
x = np.linspace(300, 710)

plt.figure(1)
plt.errorbar(U,N, xerr = 0, yerr = dN, fmt='o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label = 'Kennlinie')
plt.plot(x, params[0] * x + params[1], label = 'Plateau-Ausgleichsgerade')
plt.xlabel(r'$U [V]$')
plt.ylabel(r'$N [ Imp / 60 s]$')
plt.legend()
plt.tight_layout()
plt.savefig('build/plot1.pdf')

print(f'a = {params[0]} +- {errors[0]}')
print(f'b = {params[1]} +- {errors[1]}')
print(f'Steigung in Prozent pro 100V: {((params[0] * 500 + params[1]) - (params[0] * 400 + params[1])) / 100}')


N1= /120
N2= /120
N12= /120

n1= ufloat(N1,np.sqrt(N1))
n2= ufloat(N2, np.sqrt(N2))
n12= ufloat(N12, np.sqrt(N12))

T= (n1+n2-n12)/(2*n1*n2)
print(f'Totzeit= {T:.6f}')

#Ladungsmenge

Q = (I * 10**(-6) * t) / N
print("Q: ", Q)
Q_ele = Q / (1.602*(10**(-19)))
print("Q_ele: ", Q_ele)

Q_err = (I * 10**(-6) *t)/(N**2)*(np.sqrt(N))

print("Q_err: ", Q_err)

Q_ele_err = 1 / (1.602*(10**(-19))) * (Q_err)

print("Q_ele_err: ", Q_ele_err)


y = np.linspace(300,700,1000)

params, covariance_matrix = np.polyfit(U, Q, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))

print(f'a2 = {params[0]} +- {errors[0]}')
print(f'b2 = {params[1]} +- {errors[1]}')



plt.figure(2)
plt.plot(x, params[0] * x + params[1], label = 'Ausgleichsgerade')
plt.plot(U, Q, 'k.', label="Ladungsmenge")
plt.errorbar(U, Q, yerr=Q_err, fmt='k.', label="Messwerte")
plt.grid()
plt.legend()
plt.xlabel(r'$U [V]$')
plt.ylabel(r'$Q [C]$')
plt.savefig("build/plot2.pdf")