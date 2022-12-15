import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

####################################Stabilisierung

def gg(L,r1,r2):
    return 1 - L *(r1+r2)/(r1*r2)+ L**2/(r1*r2)


def gg2(L, r):
    return 1-L/r

L= np.linspace(0,3,500)

plt.figure(1)
plt.plot(L, gg(L, 1.4, 1.4), '-',color='indianred',label='konkav, konkav')
plt.plot(L, gg2(L, 1.4), '-',color='maroon',label='plan, konkav')
plt.xlabel(r'Resonatorlänge $L \mathbin{/} \unit{\meter}$')
plt.ylabel(r'Stabilitätsbedingung $g1 \cdot g2$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/Stabi.pdf')


Lkk, Ikk = np.genfromtxt('content/kk.txt', unpack=True)
Lpk, Ipk = np.genfromtxt('content/pk.txt', unpack=True)
Ipk= Ipk+0.00021 #Grundintensität abziehen
Ikk= Ikk+0.00021 #Grundintensität abziehen


plt.figure(2)
<<<<<<< HEAD
plt.plot(Lkk, Ikk, 'springgreen',label='Messwerte konkav, konkav')
plt.plot(Lpk, Ipk, 'forestgreen',label='Messwerte plan, konkav')
||||||| b648f6c
plt.plot(Lkk, Ikk, 'rx',label='Messwerte konkav, konkav')
plt.plot(Lpk, Ipk, 'gx',label='Messwerte plan, konkav')
=======
plt.plot(Lkk, Ikk,'x', color='indianred',label='Messwerte konkav, konkav')
plt.plot(Lpk, Ipk,'x', color='maroon',label='Messwerte plan, konkav')
>>>>>>> 10bd027d990c666295b4cd69ecbb38f135010bf2
plt.xlabel(r'Resonatorlänge $L \mathbin{/} \unit{\centi\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\milli\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/kkpk.pdf')

##################################################################################TEM00

r00, I00 = np.genfromtxt('content/TEM00.txt', unpack=True)

#r00= r00 * 10**-2   #Abstand in Meter
I00 = I00+0.21      #Grundintensität abziehen
#I00= I00 * 10**-6  #Intensität in Watt

def Tem0(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) #Ausgleichsfunktion TEM00

params1, cov1= curve_fit(Tem0, r00, I00)
errors1 = np.sqrt(np.diag(cov1))
I01= ufloat(params1[0],errors1[0])
r01= ufloat(params1[1],errors1[1])
w01= ufloat(params1[2],errors1[2])

print('I01 =', params1[0], '±', errors1[0])
print('r01 =', params1[1], '±', errors1[1])
print('w01 =', params1[2], '±', errors1[2])

z = np.linspace(np.min(r00), np.max(r00), 500)

plt.figure(3)
plt.plot(r00, I00, 'x', color='peru',label='Messwerte')
plt.plot(z, Tem0(z,*params1),'-',color='orange', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM00.pdf')

##################################################################################TEM10

r10, I10 = np.genfromtxt('content/TEM10.txt', unpack=True)

I10 = I10+0.21      #Grundintensität abziehen


def Tem1(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) * (8*(x-r0)**2)/w**2 #Ausgleichsfunktion TEM10

params2, cov2= curve_fit(Tem1, r10, I10)
errors2 = np.sqrt(np.diag(cov2))
I02= ufloat(params2[0],errors2[0])
r02= ufloat(params2[1],errors2[1])
w02= ufloat(params2[2],errors2[2])

print('I02 =', params2[0], '±', errors2[0])
print('r02 =', params2[1], '±', errors2[1])
print('w02 =', params2[2], '±', errors2[2])

z2 = np.linspace(np.min(r10), np.max(r10), 500)

plt.figure(4)
plt.plot(r10, I10, 'x', color='gold',label='Messwerte')
plt.plot(z2, Tem1(z2,*params2),'-',color='yellow', label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM10.pdf')


##################################################################################TEM20

r20, I20 = np.genfromtxt('content/TEM20.txt', unpack=True)

I20 = I20+0.21      #Grundintensität abziehen


def Tem2(x ,I0, r0, w):
    return I0 * np.exp(-(x-r0)**2/(2*w**2)) *( (64 *(x-r0)**4)/w**4 -(32*(x-r0)**2)/w**2 +4)#Ausgleichsfunktion TEM20

<<<<<<< HEAD
params3, cov3= curve_fit(Tem2, r20, I20) #passt irgendwie noch nicht so ganz
||||||| b648f6c
params3, cov3= curve_fit(Tem2, r20, I20) #passt irgendwie noch nciht so ganz
=======
params3, cov3= curve_fit(Tem2, r20, I20, bounds=([0.00026,0,4],np.inf))#passt irgendwie noch nciht so ganz
>>>>>>> 10bd027d990c666295b4cd69ecbb38f135010bf2
errors3 = np.sqrt(np.diag(cov3))
I03= ufloat(params3[0],errors3[0])
r03= ufloat(params3[1],errors3[1])
w03= ufloat(params3[2],errors3[2])

print('I03 =', params3[0], '±', errors3[0])
print('r03 =', params3[1], '±', errors3[1])
print('w03 =', params3[2], '±', errors3[2])

z3 = np.linspace(np.min(r20), np.max(r20), 500)

plt.figure(5)
plt.plot(r20, I20, 'x', color='forestgreen',label='Messwerte')
plt.plot(z3, Tem2(z3,*params3),'-',color='springgreen',label='Regressionsgerade')
plt.xlabel(r'Abstand $r \mathbin{/} \unit{\milli\meter}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/TEM20.pdf')




###########################################################Polarisation

phi, Ip= np.genfromtxt('content/Polarisation.txt', unpack=True)

Ip= Ip+0.00021 #Grundintensität abziehen

def Pol(x ,I0, phi0):
    return I0 * np.cos((x - phi0) * 2*np.pi / 360)**2

params4, cov4= curve_fit(Pol, phi, Ip)
errors4 = np.sqrt(np.diag(cov4))
I0p= ufloat(params4[0],errors4[0])
phi0p= ufloat(params4[1],errors4[1])

print('I0p =', params4[0], '±', errors4[0])
print('phi0p =', params4[1], '±', errors4[1])

z4 = np.linspace(np.min(phi), np.max(phi), 500)

plt.figure(6)
plt.plot(phi, Ip, 'x', color='darkcyan',label='Messwerte')
plt.plot(z4, Pol(z4,*params4),'-',color='cyan', label='Regressionsgerade')
plt.xlabel(r'Winkel $\phi\mathbin{/} \unit{\degree}$')
plt.ylabel(r'Intensität $I \mathbin{/} \unit{\milli\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/Pol.pdf')



#############################################Gitter


l1= 87.6 #Abstände Schirm und Gitter
l2= 92
l3= 86.3
l4= 42.7

n1,d1 =np.genfromtxt('content/80.txt', unpack=True)
n2,d2 =np.genfromtxt('content/100.txt', unpack=True)
n3,d3 =np.genfromtxt('content/600.txt', unpack=True)
n4,d4 =np.genfromtxt('content/1200.txt', unpack=True)

g1= 80* 1e3 #Gitterkonstanten
g2= 100* 1e3
g3= 600* 1e3
g4= 1200* 1e3

def lam(n,d,l,g):
    return unp.sin(unp.tan(d/l))/ (g*n)

lam1 = lam(n1, d1, l1, g1)
lam2 = lam(n2, d2, l2, g2)
lam3 = lam(n3, d3, l3, g3)
lam4 = lam(n4, d4, l4, g4)

lam = np.array((np.mean(lam1),np.mean(lam2),np.mean(lam3),np.mean(lam4)))
print(lam)

print('lam1 = ', np.mean(lam1)*1e9,'+-',np.std(lam1)*1e9)

print('lam2 = ', np.mean(lam2)*1e9,'+-',np.std(lam2)*1e9)
print('lam3 = ', np.mean(lam3)*1e9,'+-',np.std(lam3)*1e9)
print('lam4 = ', np.mean(lam4)*1e9,'+-',np.std(lam4)*1e9)
print('lam = ', np.mean(lam) *1e9,'+-',np.std(lam)*1e9)



