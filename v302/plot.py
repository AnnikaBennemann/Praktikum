import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
<<<<<<< HEAD
import uncertainties as un
||||||| 3fd3127
import uncertainties
=======
import uncertainties as un
from uncertainties.umath import *
>>>>>>> 017c9493bf7b4375f29a9d0a852d1445d0e5ce81

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
print('aaaaaaaaaaaaaaaaaaa')
R2=np.array([332,500,1000])
R3=np.array([420,325,194])
R4=np.array([580,675,806])
Rx = R2*(R3/R4)
print('R_x ', Rx)
print('Mittelwert ' ,np.mean(Rx))
print('Standardabweichung', np.std(Rx))
print('Fehler des Mittelwertes ' ,np.std(Rx)/np.sqrt(3))
Rx= un.ufloat(np.mean(Rx),np.std(Rx)/np.sqrt(3))
Rtheo=239 
abw = 100 * (Rx - Rtheo)/Rtheo

print(f'Abw theorie {abw:.2f}')

#################################b
<<<<<<< HEAD
R2=un.ufloat(192,0.02*192)
R3= 691
R4= 309
R34= un.ufloat(R3/R4,0.05*R3/R4)
C2= un.ufloat(992, 0.02)
Rx=R2*R34
print('Rx',Rx)
||||||| 3fd3127
R2=ufloat(192,0.02*192)
R3= 691
R4= 309
R34= (R3/R4 , 0.05)
C2= ufloat(992, 0.02)
Rx=R2*R34
print('Rx',Rx)
=======
print('bbbbbbbbbbbbbbbbbbb')
print('Wert 9')
R2=un.ufloat(192.00, 0.002*192.00)
R3= 691.00
R4= 309.00
R34=un.ufloat(R3/R4 , 0.005*R3/R4)
R43=un.ufloat(R4/R3 , 0.005*R4/R3)
C2= un.ufloat(992 * 10**(-9), 992 * 10**(-9)*0.002)
Rx=(R2*R34)
Rtheo= 464.9
abw = 100 * (Rx - Rtheo)/Rtheo
print('R2',R2, 'R3', R3, 'R4', R4)
print(f'Rx {Rx:.2f}')
print(f'Abw theorie {abw:.2f}')
Cx= (C2*R43)
Ctheo= 433.71*10**(-9)
abw = 100 * (Cx - Ctheo)/Ctheo
print(f'Cx {Cx:.4e}')
print(f'Abw theorie {abw:.2f}')

print('Wert 1')
R2=0
R3= 605.00
R4= 395.00
R34=un.ufloat(R3/R4 , 0.005*R3/R4)
R43=un.ufloat(R4/R3 , 0.005*R4/R3)
C2= un.ufloat(992 * 10**(-9), 992 * 10**(-9)*0.002)
Rx=(R2*R34)
print('R2',R2, 'R3', R3, 'R4', R4)
print(f'Rx {Rx:.2f}')
Cx= (C2*R43)
Ctheo= 660*10**(-9)
abw = 100 * (Cx - Ctheo)/Ctheo
print(f'Cx {Cx:.4e}')
print(f'Abw theorie {abw:.2f}')


################################c
print('cccccccccccccccccccc')
R2=un.ufloat(59.00, 0.002*59.00)
R3= 609.00
R4= 391.00
R34=un.ufloat(R3/R4 , 0.005*R3/R4)
L2= un.ufloat(27.5 * 10**(-3), 27.5 * 10**(-3)*0.002)
Rx=(R2*R34)
print('R2',R2, 'R3', R3, 'R4', R4)
print(f'Rx {Rx:.2f}')
Rtheo= 93.65
abw = 100 * (Rx - Rtheo)/Rtheo
print(f'Abw theorie {abw:.2f}')
Lx= (L2*R34)
Ltheo= 41.85*10**(-3)
abw = 100 * (Lx - Ltheo)/Ltheo
print(f'Lx {Lx:.4e}')
print(f'Abw theorie {abw:.2f}')

###############################d
print('ddddddddddddddddddddd')
R2=un.ufloat(500.00, 0.002*500.00)
R3= un.ufloat(291.00, 0.03*291.00)
R4= un.ufloat(1000.00, 0.03*1000.00)
C4= un.ufloat(450 * 10**(-9), 450 * 10**(-9)*0.002)
Rx=(R2*R3/R4)
print('R2',R2, 'R3', R3, 'R4', R4)
print(f'Rx {Rx:.2f}')
Rtheo= 93.65
abw = 100 * (Rx - Rtheo)/Rtheo
print(f'Abw theorie {abw:.2f}')
Lx= (R2*R3*C4)
Ltheo= 41.85*10**(-3)
abw = 100 * (Lx - Ltheo)/Ltheo
print(f'Lx {Lx:.4e}')
print(f'Abw theorie {abw:.2f}')

##############################e
print('eeeeeeeeeeeeeeeeeeeee')
U2=U_Br[6]/f(2,1)
U1=10
k=U2/U1
print(f'U2 {U2}')
print(f'Klirrfaktor {k}')




>>>>>>> 017c9493bf7b4375f29a9d0a852d1445d0e5ce81
