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
print('Plateaumittelwert =' , HoeheP)

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
#plt.plot(tv, n, 'rx',label='Messwerte')
plt.errorbar(tv, n, yerr=np.sqrt(n), fmt='rx', label="Messwerte")
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
params3, cov3= curve_fit(fit, K, tk)
errors3 = np.sqrt(np.diag(cov3))
a3= ufloat(params3[0],errors3[0])
b3= ufloat(params3[1],errors3[1])
print('a3 =', params3[0], '±', errors3[0])
print('b3 =', params3[1], '±', errors3[1])

plt.figure(2)
plt.plot(K, tk, 'rx',label='Messwerte')
plt.plot(K, fit(K,*params3),'-', label='Regressionsgerade')
plt.xlabel(r'Channel')
plt.ylabel(r'$\Delta t \mathbin{/} \unit{\micro\second}$')
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
Daten= Daten -3
ch = np.linspace(0,512,512)
ch_plot= np.linspace(4,440,436)

def exp(t, N, tau,U):
	return N*np.exp(-t/tau)+U

params4, cov4 = curve_fit(exp,ch_plot, Daten[4:440]) #Exponentialfunktionsfit
errors4 = np.sqrt(np.diag(cov4))
N = ufloat(params4[0], errors4[0])
tau = ufloat(params4[1], errors4[1])
U = ufloat(params4[2], errors4[2])
mittLebens=a3 *tau +b3 #Lebensdauer berechnen mit der ausgleichsgerade von der kalibrierung
abw= (mittLebens-2.20)/2.20 *100 #keine Ahnung warum da falsche werte rausgespuckt werden. Mit dem Taschenrechner kommt das richtige raus
print('N =' , N,
       'U =' , U,
       'tau =' , tau,
       'lebensdauer =' , mittLebens,
       'Abweichung = ', abw
       )


plt.figure(3)
plt.errorbar(ch_plot, Daten[4:440], yerr=np.sqrt(Daten[4:440]), fmt='rx', elinewidth=0.7, label="Messdaten",markersize=3, capsize=1.5, markeredgewidth=0.5)
#plt.step(ch, Daten,'rx', label='Messwerte')
plt.plot(ch_plot, exp(ch_plot,*params4),'-', label='Regressionsgerade')
plt.xlabel('Kanal')
plt.ylabel('Anzahl an Impulse')
plt.grid()
plt.legend(loc='best', numpoints=1)
plt.tight_layout()
plt.savefig('build/plot3.pdf')

