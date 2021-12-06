import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import uncertainties as un

from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit


v, U_Br = np.genfromtxt('content/Messwerte.txt', unpack=True)

v_0 = 241.14
y = U_Br/10 #U_Br / U_S
print(v_0)

def f(w,g):
    return np.sqrt(((w/g)**2-1)**2/(9*((1-(w/g)**2)**2+9*(w/g)**2)))



#dist1 =np.sqrt(np.square((y)-f(v,v_0)))
#dist2 =np.sqrt(1/24 *np.sum(np.square((y)-f(v,v_0))))
#mdist1=np.mean(dist1)


#print(mdist1,dist2)


#### noch rausfinden v_0, cov = curve_fit(f, v, U, p0=(v_0))

x=np.linspace(0.07,100, 20000)
#z=(f(x))


plt.figure()
plt.plot(v/v_0, y,'rx', label='Messdaten')
plt.plot(x,np.sqrt((x**2-1)**2/(9*((1-x**2)**2+9*x**2))) , 'c', label='Theoretische Werte')
plt.xscale('log')
plt.xlabel(r'$\Omega = \nu / \nu_0$')
plt.ylabel(r'$U_Br / U_S$')
plt.legend(loc='best')
plt.grid()


# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

##############################a
R2=np.array([332,500,1000])
R3=np.array([420,325,194])
R4=np.array([580,675,806])
Rx = R2*(R3/R4)
print('R_x ', Rx)
print('Mittelwert ' ,np.mean(Rx))
print('Standardabweichung', np.std(Rx))
print('Fehler des Mittelwertes ' ,np.std(Rx)/np.sqrt(3))

#################################b
R2=un.ufloat(192,0.02*192)
R3= 691
R4= 309
R34= un.ufloat(R3/R4,0.05*R3/R4)
C2= un.ufloat(992, 0.02)
Rx=R2*R34
print('Rx',Rx)
