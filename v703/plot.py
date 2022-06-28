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
N_=unp.uarray(N,dN)
print(f'N = ', N_)
#Up = U[5:-7]
#Np = N[5:-7]

params, covariance_matrix = np.polyfit(U, N, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))
x = np.linspace(320, 700)

plt.figure(1)
plt.errorbar(U,N, yerr = dN, fmt='o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label = 'Messwerte')
plt.plot(x, params[0] * x + params[1], label = 'Plateau-Ausgleichsgerade')
plt.xlabel(r'$U [V]$')
plt.ylabel(r'$N [ $Impulse$ /s]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')

print(f'a = {params[0]} +- {errors[0]}')
print(f'b = {params[1]} +- {errors[1]}')
prozent=(N_[38]/N_[0]-1)*100*100/380
print(f'Steigung in Prozent pro 100V:{prozent:.2f}'  )


N1= 87579/120
N2= 126615/120
N12= 199854/120

n1= ufloat(N1,np.sqrt(N1))
n2= ufloat(N2, np.sqrt(N2))
n12= ufloat(N12, np.sqrt(N12))

T= (n1+n2-n12)/(2*n1*n2)
print(f'Totzeit= {T:.6f}')

#Ladungsmenge

Q = (I * 10**(-6)) / N
print("Q: ", Q)
Q_ele = Q / (1.602*(10**(-19)))
print("Q_ele: ", Q_ele)

Q_err = (I * 10**(-6))/(N**2)*(np.sqrt(N))

print("Q_err: ", Q_err)

Q_ele_err = 1 / (1.602*(10**(-19))) * (Q_err)

print("Q_ele_err: ", Q_ele_err)


y = np.linspace(320,700,1000)

params, covariance_matrix = np.polyfit(U, Q_ele, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))

print(f'a2 = {params[0]} +- {errors[0]}')
print(f'b2 = {params[1]} +- {errors[1]}')



plt.figure(2)
plt.plot(x, params[0] * x + params[1], label = 'Ausgleichsgerade')
plt.errorbar(U,Q_ele, yerr = Q_ele_err, fmt='o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5, label = 'Messwerte')
plt.grid()
plt.legend(loc='best')
plt.xlabel(r'$U [V]$')
plt.ylabel(r'$Z $')
plt.tight_layout()
plt.savefig("build/plot2.pdf")

