import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit


tv, n = np.genfromtxt('content/verzögerung.txt', unpack=True)
tv
n = n/40 # counts in counts pro sekunde
def fit(x ,a, b):
    return a*x+b

params1, cov1= curve_fit(fit, tv[0:10], n[0:10])
params2, cov2= curve_fit(fit, tv[34:44], n[34:44])
errors1 = np.sqrt(np.diag(cov1))
errors2 = np.sqrt(np.diag(cov2))
a1= ufloat(params1[0],errors1[0])
b1= ufloat(params1[1],errors1[1])
a2= ufloat(params2[0],errors2[0])
b2= ufloat(params2[1],errors2[1])
print('a1 =', params1[0], '±', errors1[0])
print('b1 =', params1[1], '±', errors1[1])
print('a2 =', params2[0], '±', errors2[0])
print('b2 =', params2[1], '±', errors2[1])

plt.plot(tv[0:10], fit(tv[0:10],*params1),'-', label='Regression für Anstieg')
plt.plot(tv[34:44], fit(tv[34:44],*params2),'b-', label='Regression für Abfall')

#Halbwertsbreite berechnen
HoeheP_val= np.mean(n[10:34])
HoeheP_std= np.std(n[10:34])
HoeheP = ufloat(HoeheP_val,HoeheP_std)
print('Plataumittelwert =' , HoeheP)

cl = 1/(a1) * (HoeheP_val/2 - b1)
print('cl =' , cl)
cr = 1/(a2) * (HoeheP_val/2 - b2)
print('cr =' , cr)
d = cr -cl
print('d =' , d)

x1=np.linspace(-20, 25, 100)
plt.plot(x1, 0*x1 + HoeheP_val, 'g-', linewidth = 1.1, label = r'Plateaumittelwert')
plt.plot(x1, 0*x1 + HoeheP_val/2, 'g--', linewidth = 1.1, label = r'Plateaumittelwert/2')

#Justage plot
plt.figure(1)
plt.plot(tv, n, 'rx',label='Messwerte')
plt.ylabel(r'counts $n \mathbin{/} \unit{\per\second}$')
plt.xlabel(r'$\Delta t \mathbin{/} \unit{\nano\second}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/plot1.pdf')


x= (params2[1]-params1[1])/(params1[0]-params2[0])
print('Schnittpunkt also Verzögerung einstellen auf ', x)


#Lineare Anpassung zu den Kanälen
tk, K= np.genfromtxt('content/channel.txt', unpack=True)
params3, cov3= curve_fit(fit, tk, K)
errors3 = np.sqrt(np.diag(cov3))

print('a3 =', params3[0], '±', errors3[0])
print('b3 =', params3[1], '±', errors3[1])

plt.figure(2)
plt.plot(tk, K, 'rx',label='Messwerte')
plt.plot(tk, fit(tk,*params3),'-', label='Regressionsgerade')
plt.ylabel(r'Channel')
plt.xlabel(r'$t \mathbin{/} \unit{\micro\second}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/plot2.pdf')


#Untergrund berechnen
Nstart = ufloat(4747339, np.sqrt(4747339))
#print('Nstart =' , Nstart)
Nstop = 21974
tges = 169832.86
Ts= 10 * 10**-6


Imess = Nstart/tges
print('Imess =' , Imess)

mu = Imess * Ts
#print('mu =' , mu)
pmu = mu * unp.exp(-mu)
#print('pmu =' , pmu)

Ug = pmu * Nstart
print('Ug =' , Ug)
Un = Ug/435 #Anzahl der relevanten Kanäle
print('Un =' , Un)

#Grafik
Daten= np.genfromtxt('content/messung.txt', unpack=True)
ch = np.linspace(4,512, 512)





plt.figure(3)
plt.step(ch, Daten,'rx', label='Messwerte')
plt.xlabel('Kanal')
plt.ylabel('Anzahl an Impulse')

plt.grid()
plt.legend(loc='best', numpoints=1)
plt.tight_layout()
plt.savefig('build/plot3.pdf')

def exp(t, N, tau, U):
	return N*np.exp(-t/tau) + U

#params, cov = curve_fit(exp,, daten)
#errors = np.sqrt(np.diag(cov))
#N = ufloat(params[0], errors[0])
#tau = ufloat(params[1], errors[1])
#U = ufloat(params[2], errors[2])
#
#print('N =' , N,
#       'U =' , U,
#       'tau =' , tau)