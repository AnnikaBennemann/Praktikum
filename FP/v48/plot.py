import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from numpy import exp
from numpy import sqrt
import scipy.constants as const
from uncertainties import ufloat_fromstr
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
import math
import scipy.constants as sc
from scipy import integrate


t, T, I= np.genfromtxt('content/Messung1.txt', unpack=True)
ta, Ta, Ia= np.genfromtxt('content/Messung1abzug.txt', unpack=True)
tk, Tk, Ik =np.genfromtxt('content/Messung1Korrektur.txt', unpack=True)
tf, Tf, If= np.genfromtxt('content/Messwerte1korr.txt', unpack=True)

#Temperatur in K
T=T+273.15 
Ta=Ta+273.15
Tk=Tk+273.15
Tf=Tf+273.15
#t=np.arange(0, 50)

#Mittlere Heizrate bestimmen
diff=np.diff(T)

print('Mittelwert Heizrate diff=', np.mean(diff), sem(diff))
H=ufloat(np.mean(diff),sem(diff))
print('Heizrate=', H)

######Plot/Fit Untergrund########

plt.figure(1)
x = np.linspace(210, 316)
plt.plot (T, I,'r+', label='Messdaten')
plt.plot (Ta, Ia,'yx', label='Messdaten für Fit')

def fit(x ,a, b):
    return a*np.exp(-b/x)

params, cov= curve_fit(fit, Ta, Ia)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
plt.plot(x, fit(x,*params),'b-', label='Regression')

# Gauss funktion
  
def gauss(x, H, A, x0, sigma):
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
m = np.mean(Tk)
sigma = np.std(Tk)

def gauss_fit(x, y):
    popt, pcov = curve_fit(gauss, Tk, Ik, p0=[min(Ik), max(Ik), m, sigma])
    return popt
plt.plot(Tk, gauss(Tk, *gauss_fit(Tk, Ik)), '-', label='Gauss-Fit')

plt.plot(Tf[12:16],If[12:16], 'k+', label= 'korrigierte Werte')
#print(gauss(238.55, *gauss_fit(Tk, Ik)))
#print(gauss(240.55, *gauss_fit(Tk, Ik)))
#print(gauss(242.55, *gauss_fit(Tk, Ik)))
#print(gauss(244.55, *gauss_fit(Tk, Ik)))
#print(gauss(246.45, *gauss_fit(Tk, Ik)))

H, A, x0, sigma = gauss_fit(Tk, Ik)
FWHM = 2.35482 * sigma

#print('The offset of the gaussian baseline is', H)
#print('The center of the gaussian fit is', x0)
#print('The sigma of the gaussian fit is', sigma)
#print('The maximum intensity of the gaussian fit is', H + A)
#print('The Amplitude of the gaussian fit is', A)
#print('The FWHM of the gaussian fit is', FWHM)

plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in $A \cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot1.pdf')

#Untergrund abziehen
plt.figure(2)
Iohne=If-fit(Tf,*params)
#print('I ohne Untergrund=',Iohne)
plt.plot(Tf, Iohne,'r+', label='Messdaten ohne Untergrund')
plt.plot(Tf[5:30], Iohne[5:30],'b+', label='Messdaten für Integral')
plt.plot(Tf[5:22], Iohne[5:22],'k+', label='Messdaten für Anlaufkurve')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in $A \cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout() 
plt.savefig('build/plot2.pdf')





##########################Messung2  #########################################################################################################
t2, T2, I2= np.genfromtxt('content/Messung2.txt', unpack=True)
ta2, Ta2, Ia2= np.genfromtxt('content/Messung2abzug.txt', unpack=True)
tk2, Tk2, Ik2 =np.genfromtxt('content/Messung2Korrektur.txt', unpack=True)
tf2, Tf2, If2= np.genfromtxt('content/Messwerte2korr.txt', unpack=True)


T2=T2+273.15 #Temperatur in K
Ta2=Ta2+273.15
Tk2=Tk2+273.15
Tf2=Tf2+273.15
#t=np.arange(0, 50)

#Mittlere Heizrate bestimmen
diff=np.diff(T2)

print('Mittelwert Heizrate diff=', np.mean(diff), sem(diff))
H=ufloat(np.mean(diff),sem(diff))
print('Heizrate=', H)

######Plot/Fit Untergrung########

plt.figure(3)
x2 = np.linspace(205, 316)
plt.plot (T2, I2,'r+', label='Messdaten')
plt.plot (Ta2, Ia2,'yx', label='Messdaten für Fit')


params, cov= curve_fit(fit, Ta2, Ia2)
errors = np.sqrt(np.diag(cov))
print('a2 =', params[0], '±', errors[0])
print('b2 =', params[1], '±', errors[1])

plt.plot(x2, fit(x2,*params),'b-', label='Regression')


m2 = np.mean(Tk2)
sigma2 = np.std(Tk2)

def gauss_fit(x, y):
    popt, pcov = curve_fit(gauss, Tk2, Ik2, p0=[min(Ik2), max(Ik2), m2, sigma2])
    return popt
plt.plot(Tk2, gauss(Tk2, *gauss_fit(Tk2, Ik2)), '-', label='Gauss-Fit')

plt.plot(Tf2[22:28],If2[22:28], 'k+', label= 'korrigierte Werte')
#print(gauss(241.15, *gauss_fit(Tk2, Ik2)))
#print(gauss(242.35, *gauss_fit(Tk2, Ik2)))
#print(gauss(243.65, *gauss_fit(Tk2, Ik2)))
#print(gauss(244.95, *gauss_fit(Tk2, Ik2)))
#print(gauss(246.45, *gauss_fit(Tk2, Ik2)))
#print(gauss(247.95, *gauss_fit(Tk2, Ik2)))
#print(gauss(249.55, *gauss_fit(Tk2, Ik2)))

plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in $A \cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot3.pdf')


#Untergrund abziehen
plt.figure(4)
Iohne2=If2-fit(Tf2,*params)
#print('I ohne Untergrund=',Iohne2)
plt.plot(Tf2, Iohne2,'r+', label='Messdaten ohne Untergrund')
plt.plot(Tf2[10:43], Iohne2[10:43],'b+', label='Messdaten für Integral')
plt.plot(Tf2[10:29], Iohne2[10:29],'k+', label='Messdaten für Anlaufkurve')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in $A \cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout() 
plt.savefig('build/plot4.pdf')



#####Aktiviungsarbeit aus Anlaufkurve#########################################################################################################
plt.figure(5)
#u = np.linspace(0.0039, 0.0045)
TAnlauf=Tf[5:22]
IAnlauf=np.log(Iohne[5:22])
plt.plot(1/TAnlauf, IAnlauf,'r+', label='Messdaten')


def g(x ,c, d):
    return -c*x+d

params, cov= curve_fit(g, 1/TAnlauf,  IAnlauf)
errors = np.sqrt(np.diag(cov))
print('c =', params[0], '±', errors[0])
print('d =', params[1], '±', errors[1])

#plt.plot(u, g(u,*params),'b-', label='Regression')
plt.plot(1/TAnlauf, g(1/TAnlauf,*params),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in 1/K')
plt.ylabel(r'ln$(I)$ in ln($A\cdot 10^{-11}$)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot5.pdf')


W1A=ufloat(params[0],errors[0])*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Anlauf (eV)=', W1A)


#####Polarisationsansatz/ Integral
Tint=Tf[5:30] #Für Integral verwendete Werte
Iint=Iohne[5:30] #Für Integral verwendete Werte
I_int = integrate.cumtrapz(Iint, Tint, initial=Iint[0]) #Integral berechnen
IInt=np.log(I_int/Iint)
#print('Iint', Iint)
#print('Tint', Tint)
#print('I_int', I_int)
#print('IInt=', IInt)


############ Ohne log
plt.figure(6)
plt.plot(1/Tint, I_int/Iint ,'r+', label='Integral')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$f(T)$ in $A\cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot6.pdf')

###############
plt.figure(7)
plt.plot(1/Tint, IInt ,'r+', label='Integral')
t = np.linspace(0.00365, 0.0045)
def h(x ,e, f):
    return -e*x+f

params3, cov3= curve_fit(h, 1/Tint,  IInt)
errors3 = np.sqrt(np.diag(cov3))
print('e =', params3[0], '±', errors3[0])
print('f =', params3[1], '±', errors3[1])

plt.plot(1/Tint, h(1/Tint,*params3),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'ln$f(T)$ in $A\cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot7.pdf')


W1I=ufloat(params3[0],errors3[0])*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Integral (eV)=', W1I)

####Relaxationszeit
Tmax=259.45 #K
taumax1A=(const.k*Tmax**2)/(H*W1A)
taumax1I=(const.k*Tmax**2)/(H*W1I)

print('Relaxationszeit Anlauf=', taumax1A)
print('Relaxationszeit Integral=', taumax1I)


##################################################Messung2  ##############################################################################


plt.figure(8)
#u = np.linspace(0.0039, 0.0045)
TAnlauf=Tf2[10:29]
IAnlauf=np.log(Iohne2[10:29])
plt.plot(1/TAnlauf, IAnlauf,'r+', label='Messdaten')


def g(x ,c, d):
    return -c*x+d

params, cov= curve_fit(g, 1/TAnlauf,  IAnlauf)
errors = np.sqrt(np.diag(cov))
print('c =', params[0], '±', errors[0])
print('d =', params[1], '±', errors[1])

#plt.plot(u, g(u,*params),'b-', label='Regression')
plt.plot(1/TAnlauf, g(1/TAnlauf,*params),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in 1/K')
plt.ylabel(r'ln$(I)$ in ln($A\cdot 10^{-11}$)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot8.pdf')


W2A=ufloat(params[0],errors[0])*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Anlauf (eV)=', W2A)


#####Polarisationsansatz/ Integral
Tint=Tf2[10:43] #Für Integral verwendete Werte
Iint=Iohne2[10:43] #Für Integral verwendete Werte
I_int = integrate.cumtrapz(Iint, Tint, initial=Iint[0]) #Integral berechnen
IInt=np.log(I_int/Iint)
#print('Iint', Iint)
#print('Tint', Tint)
#print('I_int', I_int)
#print('IInt=', IInt)


############ Ohne log
plt.figure(9)
plt.plot(1/Tint, I_int/Iint ,'r+', label='Integral')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$f(T)$ in $A\cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot9.pdf')

###############
plt.figure(10)
plt.plot(1/Tint, IInt ,'r+', label='Integral')
t = np.linspace(0.00365, 0.0045)
def h(x ,e, f):
    return -e*x+f

params3, cov3= curve_fit(h, 1/Tint,  IInt)
errors3 = np.sqrt(np.diag(cov3))
print('e =', params3[0], '±', errors3[0])
print('f =', params3[1], '±', errors3[1])

plt.plot(1/Tint, h(1/Tint,*params3),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'ln$f(T)$ in $A\cdot 10^{-11}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot10.pdf')


W2I=ufloat(params3[0],errors[0])*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Integral (eV)=', W2I)

####Relaxationszeit
Tmax=249.55 #K
taumax2A=(const.k*Tmax**2)/(H*W2A)
taumax2I=(const.k*Tmax**2)/(H*W2I)

print('Relaxationszeit Anlauf=', taumax2A)
print('Relaxationszeit Integral=', taumax2I)