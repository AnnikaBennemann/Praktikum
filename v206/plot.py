import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

t, T2, pa, T1, pb, N = np.genfromtxt('content/Messung.txt', unpack=True)

t *= 60 #Zeit in Sekunden
T1 += 273.15 #Temperatur in Kelvin
T2 += 273.15
pa += 1 #Druck plus 1 bar 
pb += 1
mkck= 750
m1= 3
cw= 4182
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb



x = np.linspace(t[0], t[31], 100)

def T_t(x, a, b, c):
    return a*x**2+b*x+c

params, cov = curve_fit(T_t, t, T1)
a, b, c = params[0], params[1], params[2]
yfit1 = a*x**2+b*x+c
errors = np.sqrt(np.diag(cov))
print('T1 a,b,c = ', params)
print('errors = ', errors)
a, b, c = ufloat(params[0], errors[0]), ufloat(params[1], errors[1]), ufloat(params[2], errors[2])


params, cov = curve_fit(T_t, t, T2)
errors1 = np.sqrt(np.diag(cov))
a2, b2, c2 = params[0], params[1], params[2]
yfit2 = a2*x**2+b2*x+c2
print('T2 a,b,c = ', params)
print('errors = ', errors1)
a2, b2, c2 = ufloat(params[0], errors1[0]), ufloat(params[1], errors1[1]), ufloat(params[2], errors1[2])


plt.figure(1)
plt.plot(t, T1, 'rx', label='T1')
plt.plot(t, T2, 'bx', label='T2')
plt.plot(x, yfit1, 'r-', label= 'Ausgleichsgerade T1')
plt.plot(x, yfit2, 'b-', label= 'Ausgleichsgerade T2')
plt.ylabel(r'Zeit $t \mathbin{/} \si{\second}$')
plt.xlabel(r'Temperatur $T \mathbin{/} \si{\kelvin}$')

plt.grid()
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')

#ccccccccccccccccccccccccccccccccccccccccccccccc

def dT(x,a,b):
    return 2*a*x+b

q= (7,14,21,28)
for i in q:

    dT1=dT(T1[i],a,b)
    dT2=dT(T2[i],a2,b2)
    print('dT1/dt', i, dT1) #Differenzenquotienten
    print('dT2/dt', i, dT2)

#ddddddddddddddddddddddddddddddddddddddddddddddd

Nm=ufloat(np.mean(N),np.std(N)/np.sqrt(len(N)))
print('Nm=', Nm) #gemittelte Leistungsaufnahme Kompressor

for i in q:

    v=(m1*cw+mkck)*dT(T1[i],a,b)/Nm
    vid = T1[i]/(T1[i]-T2[i])
    abw = 100*(v-vid)/vid
    print('v',i, v) #güteziffer real
    print('vid',i, vid) #Güteziffer ideal
    print('abw', i, abw) 

#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

x_plot=1/T1
y_plot=np.log(pb)
xfit = np.linspace(x_plot[0],x_plot[31],100)
params, cov = np.polyfit(x_plot, y_plot, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))
a= ufloat(params[0], errors[0])
b= ufloat(params[1], errors[1])
print(f'a {a:.2f}')
print(f'b {b:.2f}')
L = (-a*8.31446261815324)
print(f'L {L:.2f}') #Verdampfungswärme

plt.figure(2)
plt.plot(x_plot, y_plot, 'rx', label='Messdaten des Reservoir 1')
plt.plot(xfit, params[0]*xfit+params[1], 'r-', label='Ausgleichsgerade')
plt.ylabel(r'$ln(\frac{pb}{p_0}$)')
plt.xlabel(r'$1/T1 \mathbin{/} \si{\per\kelvin}$')
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')

for i in q:

    dm=dT(T2[i],a2,b2)/L
    dmmol=dm*120.9
    print('dm/dt ms', i, dm) #Massendurchsatz mol pro sekunde
    print('dm/dt gs', i, dmmol) #Massendurchsatz gramm pro sekunde
    #irgendwas passt noch nicht





#fffffffffffffffffffffffffffffffffffffffffff



 